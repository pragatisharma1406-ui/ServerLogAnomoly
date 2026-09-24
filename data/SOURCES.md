# Public log dataset references

The assignment calls for a public Apache/Nginx access-log dataset. These are the public references used as provenance targets for this project:

- Kaggle — **Web Server Access Logs** (Elias Dabbas): https://www.kaggle.com/datasets/eliasdabbas/web-server-access-logs
- LogHub — **Apache** log collection: https://github.com/logpai/loghub
- SecRepo — public log samples: https://www.secrepo.com/

The packaged `data/raw/access.log` is a reproducible Apache Combined-style fixture generated locally because external dataset downloading was unavailable during packaging. Replace it with a downloaded public log when strict source provenance is required.
