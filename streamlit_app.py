import streamlit as st
import pandas as pd
import re
from pathlib import Path
from sklearn.ensemble import IsolationForest

st.set_page_config(
    page_title="Server Log Anomaly Detection",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Server Log Anomaly Detection")

st.write(
    "Analyze Apache server logs to identify unusual traffic patterns "
    "and suspicious activities."
)

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ '
    r'\[(?P<timestamp>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<url>\S+) (?P<protocol>[^"]+)" '
    r'(?P<status>\d{3}) '
    r'(?P<bytes>\S+)'
)

def parse_logs(lines):
    records = []

    for line in lines:
        match = LOG_PATTERN.match(line.strip())

        if match:
            data = match.groupdict()

            try:
                timestamp = pd.to_datetime(
                    data["timestamp"],
                    format="%d/%b/%Y:%H:%M:%S %z"
                )
            except:
                continue

            try:
                status = int(data["status"])
            except:
                status = 0

            try:
                response_bytes = int(data["bytes"])
            except:
                response_bytes = 0

            records.append({
                "IP": data["ip"],
                "Timestamp": timestamp,
                "Method": data["method"],
                "URL": data["url"],
                "Status": status,
                "Response_Bytes": response_bytes
            })

    return pd.DataFrame(records)

st.sidebar.header("📂 Log Input")

uploaded_file = st.sidebar.file_uploader(
    "Upload a new server log file",
    type=["log", "txt"]
)

if uploaded_file is not None:
    lines = uploaded_file.read().decode(
        "utf-8",
        errors="ignore"
    ).splitlines()

    st.success(
        f"New log file uploaded successfully: {len(lines)} lines"
    )

else:
    log_file = Path("data/raw/access.log")

    if not log_file.exists():
        st.error(
            "The file data/raw/access.log was not found."
        )
        st.stop()

    lines = log_file.read_text(
        errors="ignore"
    ).splitlines()

    st.success(
        f"Server log loaded successfully: {len(lines)} lines"
    )

df = parse_logs(lines)

if df.empty:
    st.error(
        "No valid Apache log entries could be parsed."
    )
    st.stop()

st.success(
    f"Successfully parsed {len(df)} log entries."
)

df["Minute"] = df["Timestamp"].dt.floor("min")

df["Is_Error"] = (
    df["Status"] >= 400
).astype(int)

df["Is_404"] = (
    df["Status"] == 404
).astype(int)

st.subheader("📊 Log Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Requests",
        len(df)
    )

with col2:
    st.metric(
        "Unique IPs",
        df["IP"].nunique()
    )

with col3:
    st.metric(
        "Error Requests",
        int(df["Is_Error"].sum())
    )

with col4:
    st.metric(
        "404 Requests",
        int(df["Is_404"].sum())
    )

st.subheader("📄 Sample Server Logs")

for line in lines[:10]:
    st.code(line)

st.subheader("📈 Request Traffic")

traffic = (
    df.groupby("Minute")
    .size()
    .reset_index(name="Requests")
)

st.line_chart(
    traffic.set_index("Minute")
)

st.subheader("🌐 HTTP Status Distribution")

status_counts = (
    df["Status"]
    .value_counts()
    .sort_index()
)

st.bar_chart(status_counts)

ip_minute_features = (
    df.groupby(["IP", "Minute"])
    .agg(
        Requests_Per_Minute=("URL", "count"),
        Unique_URLs=("URL", "nunique"),
        Average_Response_Size=("Response_Bytes", "mean"),
        Error_Ratio=("Is_Error", "mean"),
        Not_Found_Ratio=("Is_404", "mean")
    )
    .reset_index()
)

st.subheader("🚨 Anomaly Detection")

feature_columns = [
    "Requests_Per_Minute",
    "Unique_URLs",
    "Average_Response_Size",
    "Error_Ratio",
    "Not_Found_Ratio"
]

if len(ip_minute_features) >= 10:
    model = IsolationForest(
        n_estimators=150,
        contamination=0.05,
        random_state=42
    )

    ip_minute_features["Anomaly"] = model.fit_predict(
        ip_minute_features[feature_columns]
    )

    ip_minute_features["Anomaly_Score"] = model.decision_function(
        ip_minute_features[feature_columns]
    )

else:
    ip_minute_features["Anomaly"] = 1
    ip_minute_features["Anomaly_Score"] = 0

anomalies = ip_minute_features[
    ip_minute_features["Anomaly"] == -1
].copy()

normal = ip_minute_features[
    ip_minute_features["Anomaly"] == 1
]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Anomalous Windows",
        len(anomalies)
    )

with col2:
    st.metric(
        "Normal Windows",
        len(normal)
    )

with col3:
    st.metric(
        "Anomaly Rate",
        f"{(len(anomalies) / len(ip_minute_features) * 100):.2f}%"
    )

def get_reason(row):
    reasons = []

    if row["Requests_Per_Minute"] >= 20:
        reasons.append("High request rate")

    if row["Unique_URLs"] >= 5:
        reasons.append("Multiple different URLs")

    if row["Error_Ratio"] >= 0.5:
        reasons.append("High error ratio")

    if row["Not_Found_Ratio"] >= 0.5:
        reasons.append("High number of 404 responses")

    if not reasons:
        reasons.append(
            "Unusual traffic pattern detected by Isolation Forest"
        )

    return ", ".join(reasons)

if not anomalies.empty:
    anomalies["Reason"] = anomalies.apply(
        get_reason,
        axis=1
    )

if anomalies.empty:
    st.success(
        "No anomalous traffic windows were detected."
    )

else:
    st.warning(
        f"{len(anomalies)} unusual traffic windows were detected."
    )

    st.dataframe(
        anomalies[
            [
                "IP",
                "Minute",
                "Requests_Per_Minute",
                "Unique_URLs",
                "Average_Response_Size",
                "Error_Ratio",
                "Not_Found_Ratio",
                "Anomaly_Score",
                "Reason"
            ]
        ].sort_values(
            "Anomaly_Score"
        ),
        use_container_width=True,
        hide_index=True
    )

st.subheader("🕵️ Suspicious IP Analysis")

ip_summary = (
    df.groupby("IP")
    .agg(
        Total_Requests=("IP", "count"),
        Error_Requests=(
            "Is_Error",
            "sum"
        ),
        Not_Found_Requests=(
            "Is_404",
            "sum"
        ),
        Unique_URLs=(
            "URL",
            "nunique"
        )
    )
    .reset_index()
)

ip_summary["Error_Rate"] = (
    ip_summary["Error_Requests"]
    / ip_summary["Total_Requests"]
)

ip_summary = ip_summary.sort_values(
    ["Error_Requests", "Total_Requests"],
    ascending=False
)

st.dataframe(
    ip_summary.head(15),
    use_container_width=True,
    hide_index=True
)

st.subheader("🔗 Most Requested URLs")

top_urls = (
    df["URL"]
    .value_counts()
    .head(10)
)

st.bar_chart(top_urls)

st.subheader("❌ HTTP Error Analysis")

error_df = df[
    df["Status"] >= 400
]

if error_df.empty:
    st.success(
        "No HTTP error responses were found."
    )

else:
    error_counts = (
        error_df["Status"]
        .value_counts()
        .sort_index()
    )

    st.bar_chart(error_counts)

    st.dataframe(
        error_df[
            [
                "IP",
                "Timestamp",
                "Method",
                "URL",
                "Status"
            ]
        ].head(50),
        use_container_width=True,
        hide_index=True
    )

st.divider()

st.subheader("🧠 How This System Works")

st.markdown(
    """
### 1. Server Log Collection

The system reads Apache server access logs.

### 2. Log Parsing

Each log entry is converted into structured information:

- IP address
- Timestamp
- HTTP method
- Requested URL
- HTTP status
- Response size

### 3. Feature Engineering

The system creates traffic features for each IP and one-minute window:

- Requests per minute
- Number of unique URLs
- Average response size
- Error ratio
- 404 ratio

### 4. Anomaly Detection

An **Isolation Forest** model analyzes these features
and identifies unusual traffic windows.

### 5. Investigation

The dashboard provides:

- Anomalous traffic windows
- Suspicious IP addresses
- HTTP errors
- 404 activity
- Frequently requested URLs
- Reasons associated with unusual patterns

### 6. New Log Analysis

A new `.log` or `.txt` file can be uploaded from the sidebar.
The same processing and anomaly-detection pipeline is then
applied to the new data.
"""
)

st.divider()

st.caption(
    "Server Log Anomaly Detection using Isolation Forest"
)