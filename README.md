# SERVERLOGANAMOLY — Server Log Anomaly Detection with Isolation Forest

An end-to-end machine-learning project for detecting suspicious web-server behavior from Apache/Nginx-style access logs. The project converts raw request logs into **IP + 1-minute behavioral windows**, learns normal behavior with **Isolation Forest**, evaluates controlled attack scenarios, and generates a Markdown **Threat Intelligence Report** containing the flagged windows and their exact log lines.

## Project pipeline

```text
Raw Apache access.log
        ↓
Regex parsing
        ↓
Timestamp → datetime
        ↓
IP + 1-minute aggregation
        ↓
5 behavioral features
        ↓
StandardScaler
        ↓
Isolation Forest
        ↓
Anomaly windows
        ↓
Threat Intelligence Report
```

## Features engineered

For every IP in every 1-minute window:

- **Requests/minute**
- **404 error ratio**
- **Unique URLs hit**
- **Average payload size**
- **POST-request share**

This window-level approach is important because attacks are usually patterns of behavior over time rather than isolated log lines.

## Controlled attack scenarios

The included reproducible fixture contains three labeled attack sources used only for evaluation:

1. **404 burst** — rapid requests producing many 404 responses.
2. **Hidden-route scan** — probes such as `/admin`, `/.env`, `/wp-login.php`, `/.git/config`, and `/server-status`.
3. **Request flood** — a high-volume request burst against an API endpoint.

These injected events provide ground truth for checking whether the unsupervised model can recover known anomalous windows.

## Model

The project uses `sklearn.ensemble.IsolationForest` with standardized features. Contamination values from **0.01 to 0.05** are compared. The packaged default is **0.03** for this controlled fixture because it detected all injected attack windows while keeping the false-positive rate within a practical anomaly budget. This is a project-specific modeling choice, not a universal production setting; real deployments should tune it on representative traffic.

## Dataset note

`data/raw/access.log` contains a reproducible Apache Combined-style fixture with **52,904 log lines** generated for this project because the build environment could not download an external public dataset during packaging. The intended public references are documented in `data/SOURCES.md`. For an assignment requiring strict external-data provenance, replace the fixture with a downloaded Apache/Nginx access log containing at least 50,000 lines and rerun `python train.py`.

## Run locally

### 1. Install dependencies

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Train and evaluate

```bash
python train.py
```

This regenerates:

- `reports/evaluation.csv`
- `reports/window_features.csv`
- `reports/threat_intelligence_report.md`

### 3. Run inference on a new log

```bash
python infer.py path/to/access.log --contamination 0.03 --report reports/inference_report.md
```

The inference pipeline uses the same parser and feature engineering steps as training and outputs flagged IP/minute windows plus a Markdown report.

### 4. Notebook

Open `notebooks/SERVERLOGANAMOLY.ipynb` for the step-by-step workflow, feature inspection, contamination comparison, evaluation, and report generation.

## Repository structure

```text
SERVERLOGANAMOLY/
├── README.md
├── requirements.txt
├── generate_sample.py
├── train.py
├── infer.py
├── src/
│   └── log_anomaly.py
├── data/
│   ├── SOURCES.md
│   └── raw/
│       └── access.log
├── notebooks/
│   └── SERVERLOGANAMOLY.ipynb
└── reports/
    ├── evaluation.csv
    ├── window_features.csv
    └── threat_intelligence_report.md
```

## Limitations

Isolation Forest is unsupervised: it identifies behavior that is unusual relative to the observed traffic; it does not inherently understand that a URL is malicious. The attack labels in this project are controlled injections, so the evaluation demonstrates the pipeline on known scenarios rather than claiming production-grade detection accuracy.

## Skills demonstrated

**Python · Regex · Pandas · Feature Engineering · Scikit-learn · Isolation Forest · Unsupervised Anomaly Detection · Cybersecurity Analytics · Threat Intelligence Reporting**
