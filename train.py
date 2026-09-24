from pathlib import Path
import pandas as pd
from src.log_anomaly import parse_log,engineer_features,train_model,make_report,FEATURES

ROOT=Path(__file__).parent
raw=parse_log(ROOT/'data/raw/access.log')
feat=engineer_features(raw)
rows=[]
for c in [0.01,0.02,0.03,0.04,0.05]:
    _,_,res=train_model(feat,c)
    attack_ips={'198.51.100.10','198.51.100.11','198.51.100.12'}
    injected=res.ip.isin(attack_ips)
    tp=int((res.anomaly & injected).sum()); attacks=int(injected.sum()); fp=int((res.anomaly & ~injected).sum()); normal=int((~injected).sum())
    rows.append({'contamination':c,'attack_windows':attacks,'attack_windows_flagged':tp,'detection_rate':tp/attacks if attacks else 0,'normal_windows':normal,'false_positives':fp,'false_positive_rate':fp/normal if normal else 0})
evaldf=pd.DataFrame(rows); evaldf.to_csv(ROOT/'reports/evaluation.csv',index=False)
_,_,res=train_model(feat,0.03); make_report(res,raw,ROOT/'reports/threat_intelligence_report.md')
res.to_csv(ROOT/'reports/window_features.csv',index=False)
print(evaldf.to_string(index=False)); print('\nReport written.')
