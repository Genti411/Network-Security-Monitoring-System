# Gentian Hoxha
# 04/16/2025
# Network Security Monitoring System (NSMS)

## Model Training & Detection
import pyshark
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from flask import Flask, jsonify, render_template
import threading
import time
import logging
import os


### Logger setup
os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename='logs/security.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')


### Load or train anomaly detection model
def train_model():
    normal_data = np.random.normal(0, 1, (100, 4))
    model = IsolationForest(contamination=0.1)
    model.fit(normal_data)
    return model

model = train_model()


### Feature extractor from packets
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


### Packet analysis and detection
def process_packet(pkt):
    features = extract_features(pkt)
    if features is not None:
        prediction = model.predict(features)
        if prediction[0] == -1:
            log_msg = f"Anomaly Detected: {pkt.summary}"
            logging.warning(log_msg)


### Packet sniffer
def start_sniffer():
    cap = pyshark.LiveCapture(interface='eth0')
    for pkt in cap.sniff_continuously():
        process_packet(pkt)


### Flask API for basic dashboard
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

### Run monitoring in background thread
def run_monitor():
    sniffer_thread = threading.Thread(target=start_sniffer)
    sniffer_thread.daemon = True
    sniffer_thread.start()


### Entry point
if __name__ == "__main__":
    run_monitor()
    app.run(host='0.0.0.0', port=5000)

