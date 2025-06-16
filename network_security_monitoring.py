# Gentian Hoxha
# 04/16/2025
# Network Security Monitoring System (NSMS)

## Project Overview
This script represents the initial structure of a network security monitoring system that captures traffic, applies machine learning models to detect anomalies, and integrates alerting and logging features.

### Features
- Real-time network traffic capture
- Anomaly detection using Isolation Forest
- Logging of suspicious activity
- Basic monitoring dashboard with Flask
- Deployment via Docker or AWS EC2
- Test coverage and CI-ready structure

---

## 🔭 Ongoing Enhancements
We are actively working on:
- 🔍 Integrating advanced threat intelligence feeds (e.g., AbuseIPDB, MISP)
- 🎯 Improving anomaly detection precision to reduce false positives
- 🧠 Incorporating semi-supervised learning and adaptive thresholds
- 📡 Geolocation and threat severity scoring of flagged IPs

---

## 🧪 Setup Instructions

### Requirements
```bash
pip install scikit-learn pyshark Flask pandas numpy matplotlib
```

---

## 🚀 Deployment Guide

### 📦 Local Deployment
1. Clone the repository:
```bash
git clone https://github.com/yourusername/nsms.git
cd nsms
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python monitor.py
```

4. Open your browser to:
```
http://localhost:5000
```

### 🐳 Docker Deployment
1. Build the Docker image:
```bash
docker-compose build
```

2. Start the container:
```bash
docker-compose up
```

3. Access the dashboard:
```
http://localhost:5000
```

4. Logs will be saved in the `./logs/` directory on your host.

### ☁️ Deploy to AWS EC2
1. Launch a t2.medium (or better) EC2 instance with Ubuntu.
2. SSH into the instance:
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```
3. Install Docker & Git:
```bash
sudo apt update && sudo apt install -y docker.io docker-compose git
```
4. Clone your project:
```bash
git clone https://github.com/yourusername/nsms.git && cd nsms
```
5. Run the service:
```bash
sudo docker-compose up --build -d
```
6. Visit `http://your-ec2-ip:5000`

> 🔐 Don't forget to allow TCP port 5000 in your EC2 security group.

---

## 🧠 Model Training & Detection

```python
import pyshark
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from flask import Flask, jsonify, render_template
import threading
import time
import logging
import os
```

### Logger setup
```python
os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename='logs/security.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')
```

### Load or train anomaly detection model
```python
def train_model():
    normal_data = np.random.normal(0, 1, (100, 4))
    model = IsolationForest(contamination=0.1)
    model.fit(normal_data)
    return model

model = train_model()
```

### Feature extractor from packets
```python
def extract_features(pkt):
    try:
        features = [
            float(pkt.length),
            int(pkt.highest_layer == "TCP"),
            int(pkt.highest_layer == "UDP"),
            int(pkt.highest_layer == "ICMP")
        ]
        return np.array(features).reshape(1, -1)
    except Exception as e:
        logging.warning(f"Failed to extract features: {e}")
        return None
```

### Packet analysis and detection
```python
def process_packet(pkt):
    features = extract_features(pkt)
    if features is not None:
        prediction = model.predict(features)
        if prediction[0] == -1:
            log_msg = f"Anomaly Detected: {pkt.summary}"
            logging.warning(log_msg)
```

### Packet sniffer
```python
def start_sniffer():
    cap = pyshark.LiveCapture(interface='eth0')
    for pkt in cap.sniff_continuously():
        process_packet(pkt)
```

### Flask API for basic dashboard
```python
app = Flask(__name__)

@app.route("/status", methods=['GET'])
def status():
    return jsonify({"status": "Monitoring active", "model": "IsolationForest"})

@app.route("/")
def dashboard():
    try:
        with open("logs/security.log", "r") as f:
            lines = f.readlines()[-20:]
        return render_template("dashboard.html", logs=lines)
    except Exception as e:
        return f"Error loading dashboard: {e}"
```

### Run monitoring in background thread
```python
def run_monitor():
    sniffer_thread = threading.Thread(target=start_sniffer)
    sniffer_thread.daemon = True
    sniffer_thread.start()
```

### Entry point
```python
if __name__ == "__main__":
    run_monitor()
    app.run(host='0.0.0.0', port=5000)
```

---
