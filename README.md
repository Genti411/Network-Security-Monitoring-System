# Network-Security-Monitoring-System
A comprehensive monitoring solution that detects and alerts on suspicious network activities using machine learning algorithms.
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
