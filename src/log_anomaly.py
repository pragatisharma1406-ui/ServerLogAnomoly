import re
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

LOG_RE = re.compile(r'^(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>[^]]+)\] "(?P<method>\S+) (?P<url>\S+) HTTP/[^\"]+" (?P<status>\d{3}) (?P<bytes>\S+)')
FEATURES=['requests_per_minute','error_404_ratio','unique_urls','avg_payload_size','post_share']

def parse_log(path):
    rows=[]
    with open(path,encoding='utf-8',errors='ignore') as f:
        for line in f:
            m=LOG_RE.match(line.strip())
            if not m: continue
            d=m.groupdict(); d['status']=int(d['status']); d['bytes']=0 if d['bytes']=='-' else int(d['bytes']); rows.append(d)
    df=pd.DataFrame(rows)
    if df.empty: raise ValueError('No valid Apache access-log lines found.')
    df['timestamp']=pd.to_datetime(df['timestamp'],format='%d/%b/%Y:%H:%M:%S %z',errors='coerce')
    df=df.dropna(subset=['timestamp']).copy(); df['window']=df['timestamp'].dt.floor('min')
    return df

def engineer_features(df):
    g=df.groupby(['ip','window'],as_index=False)
    out=g.agg(requests_per_minute=('ip','size'),unique_urls=('url','nunique'),avg_payload_size=('bytes','mean'))
    e=df.assign(is404=(df['status']==404)).groupby(['ip','window'],as_index=False)['is404'].mean().rename(columns={'is404':'error_404_ratio'})
    p=df.assign(ispost=(df['method']=='POST')).groupby(['ip','window'],as_index=False)['ispost'].mean().rename(columns={'ispost':'post_share'})
    out=out.merge(e,on=['ip','window']).merge(p,on=['ip','window'])
    return out[['ip','window']+FEATURES]

def train_model(features,contamination=0.03,random_state=42):
    scaler=StandardScaler(); X=scaler.fit_transform(features[FEATURES]); model=IsolationForest(n_estimators=300,contamination=contamination,random_state=random_state,n_jobs=-1)
    model.fit(X); pred=model.predict(X); scores=model.decision_function(X)
    result=features.copy(); result['anomaly']=pred==-1; result['anomaly_score']=scores
    return model,scaler,result

def reason(row):
    reasons=[]
    if row.error_404_ratio>=0.8: reasons.append(f'{row.error_404_ratio:.0%} 404 ratio')
    if row.requests_per_minute>=200: reasons.append(f'{int(row.requests_per_minute)} requests/min')
    if row.unique_urls>=6: reasons.append(f'{int(row.unique_urls)} unique URLs')
    if row.post_share>=0.5: reasons.append(f'{row.post_share:.0%} POST share')
    if row.avg_payload_size>=10000: reasons.append(f'avg payload {row.avg_payload_size:.0f} bytes')
    return ', '.join(reasons) or 'Isolation Forest anomaly score'

def make_report(result,raw_df,out_path):
    flagged=result[result.anomaly].sort_values(['window','ip'])
    with open(out_path,'w',encoding='utf-8') as f:
        f.write('# Threat Intelligence Report\n\n')
        f.write(f'Generated from {len(raw_df):,} parsed log lines. Flagged windows: **{len(flagged)}**.\n\n')
        for _,r in flagged.iterrows():
            f.write(f"## {r.ip} — {r.window}\n\n")
            f.write(f"**Reason:** {reason(r)}\n\n")
            f.write('**Features:** ' + ', '.join(f'{k}={r[k]:.3f}' if isinstance(r[k],float) else f'{k}={r[k]}' for k in FEATURES) + '\n\n')
            lines=raw_df[(raw_df.ip==r.ip)&(raw_df.window==r.window)]
            f.write('**Exact log lines:**\n\n```text\n')
            # reconstruct canonical lines
            for _,x in lines.iterrows():
                ts=x.timestamp.strftime('%d/%b/%Y:%H:%M:%S %z')
                f.write(f'{x.ip} - - [{ts}] "{x.method} {x.url} HTTP/1.1" {x.status} {x.bytes} "-" "Mozilla/5.0"\n')
            f.write('```\n\n')
    return flagged
