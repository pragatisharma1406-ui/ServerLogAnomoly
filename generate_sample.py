import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

random.seed(42)
out=Path('data/raw/access.log'); out.parent.mkdir(parents=True,exist_ok=True)
start=datetime(2026,9,1,9,0,0,tzinfo=timezone.utc)
ips=[f'192.0.2.{i}' for i in range(10,61)]
urls=['/','/index.html','/products','/products/1','/products/2','/about','/contact','/login','/search?q=phone','/static/app.js','/static/style.css','/api/items','/api/items/1','/favicon.ico']
lines=[]
# benign 50k
for i in range(52000):
    t=start+timedelta(seconds=random.randint(0,7200), milliseconds=random.randint(0,999))
    ip=random.choice(ips)
    method=random.choices(['GET','POST'],weights=[0.88,0.12])[0]
    url=random.choice(urls)
    status=random.choices([200,201,204,301,304,400,401,403,404,500],weights=[55,4,4,4,8,2,2,2,18,1])[0]
    if status==404: url=random.choice(['/missing','/does-not-exist','/old-page'])
    if method=='POST': url=random.choice(['/login','/api/items','/api/search'])
    b=random.randint(120,18000)
    lines.append((t,ip,method,url,status,b))
# attacks: 404 burst, hidden route scan, request flood
attacks={
 '198.51.100.10':[], '198.51.100.11':[], '198.51.100.12':[]}
attack_start=start+timedelta(minutes=30)
for j in range(240):
    t=attack_start+timedelta(seconds=j//4)
    attacks['198.51.100.10'].append((t,'GET',random.choice(['/missing/a','/missing/b','/missing/c']),404,random.randint(50,500)))
for j,u in enumerate(['/admin','/.env','/wp-login.php','/admin/login','/.git/config','/phpmyadmin','/server-status','/backup.zip']*8):
    t=attack_start+timedelta(minutes=10,seconds=j*2)
    attacks['198.51.100.11'].append((t,'GET',u,404,random.randint(50,900)))
for j in range(600):
    t=attack_start+timedelta(minutes=50,seconds=j/10)
    attacks['198.51.100.12'].append((t,'GET','/api/items',200,random.randint(100,5000)))
for ip,arr in attacks.items():
    for t,m,u,s,b in arr: lines.append((t,ip,m,u,s,b))
lines.sort()
with out.open('w') as f:
    for t,ip,m,u,s,b in lines:
        ts=t.strftime('%d/%b/%Y:%H:%M:%S %z')
        f.write(f'{ip} - - [{ts}] "{m} {u} HTTP/1.1" {s} {b} "-" "Mozilla/5.0"\n')
print(f'generated {len(lines)} lines -> {out}')
