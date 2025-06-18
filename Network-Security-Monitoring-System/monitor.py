from scapy.all import sniff, IP
from sklearn.ensemble import IsolationForest
import json
import time

model = IsolationForest(contamination=0.01)
log_file = "alerts.json"

def capture_packet(pkt):
    if IP in pkt:
        data_point = [len(pkt)]
        score = model.decision_function([data_point])[0]
        if score < -0.1:
            alert = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "src": pkt[IP].src,
                "dst": pkt[IP].dst,
                "len": len(pkt)
            }
            with open(log_file, "a") as f:
                f.write(json.dumps(alert) + "\n")
            print("Anomaly detected:", alert)

if __name__ == "__main__":
    print("Starting packet capture...")
    sniff(prn=capture_packet, store=0)
