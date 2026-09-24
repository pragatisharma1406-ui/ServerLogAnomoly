import streamlit as st
import pandas as pd
from pathlib import Path
from sklearn.ensemble import IsolationForest

st.set_page_config(
    page_title="Server Log Anomaly Detection",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Server Log Anomaly Detection")
st.write("Apache server logs ko analyze karke suspicious activity detect karein.")

# Load log file
log_file = Path("data/raw/access.log")

if not log_file.exists():
    st.error("access.log file nahi mili!")
    st.stop()

# Read log file
lines = log_file.read_text(errors="ignore").splitlines()

st.success(f"Log file loaded successfully: {len(lines)} lines")

# Basic log information
st.subheader("📊 Log Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Log Entries", len(lines))

with col2:
    st.metric("Unique IPs", len(set(line.split()[0] for line in lines if line.strip())))

# Show sample logs
st.subheader("📄 Sample Log Entries")

sample_lines = lines[:20]

for line in sample_lines:
    st.code(line)

# Simple anomaly detection
st.subheader("🚨 Anomaly Detection")

if len(lines) >= 10:

    # Create simple features
    data = []

    for line in lines:
        parts = line.split()

        if len(parts) >= 1:
            ip = parts[0]
            data.append([ip, len(line)])

    df = pd.DataFrame(data, columns=["IP", "Log_Length"])

    # Convert IP into frequency
    ip_counts = df["IP"].value_counts()

    df["IP_Frequency"] = df["IP"].map(ip_counts)

    # Isolation Forest
    model = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    df["Anomaly"] = model.fit_predict(
        df[["Log_Length", "IP_Frequency"]]
    )

    # -1 = anomaly, 1 = normal
    anomalies = df[df["Anomaly"] == -1]

    st.metric("Detected Anomalies", len(anomalies))

    st.dataframe(anomalies, use_container_width=True)

else:
    st.warning("Anomaly detection ke liye enough log entries nahi hain.")

st.divider()

st.caption("Server Log Anomaly Detection using Isolation Forest")