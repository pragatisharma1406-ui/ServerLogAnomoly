import argparse
from pathlib import Path
from src.log_anomaly import parse_log,engineer_features,train_model,make_report
p=argparse.ArgumentParser(description='Flag anomalous IP/minute windows in Apache access logs')
p.add_argument('log_file'); p.add_argument('--contamination',type=float,default=0.03); p.add_argument('--report',default='reports/inference_report.md')
a=p.parse_args(); raw=parse_log(a.log_file); feat=engineer_features(raw); _,_,res=train_model(feat,a.contamination); make_report(res,raw,Path(a.report)); print(res[res.anomaly].to_string(index=False))
