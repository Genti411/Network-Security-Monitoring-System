from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    alerts = []
    if os.path.exists("alerts.json"):
        with open("alerts.json") as f:
            for line in f:
                try:
                    alerts.append(json.loads(line))
                except:
                    continue
    return render_template("dashboard.html", alerts=alerts)

@app.route('/api/alerts')
def api_alerts():
    if os.path.exists("alerts.json"):
        with open("alerts.json") as f:
            return jsonify([json.loads(line) for line in f if line.strip()])
    return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)
