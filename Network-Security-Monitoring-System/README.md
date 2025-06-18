# Network Security Monitoring System (NSMS)

This project implements a Python-based Network Security Monitoring System capable of capturing traffic, detecting anomalies using machine learning, and providing real-time visualization with a Flask dashboard.

## Features
- Real-time packet capture using `scapy`
- Anomaly detection via Isolation Forest (unsupervised ML)
- Alert logging and report generation
- Flask dashboard to view alerts and system status
- Docker and GitHub Actions integration

## Requirements
Install dependencies with:
```bash
pip install -r requirements.txt
```

## Running the Project

### Run manually:
```bash
python monitor.py
python app.py
```

### Or use Docker:
```bash
docker-compose up --build
```

Access dashboard at: [http://localhost:5000](http://localhost:5000)
