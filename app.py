from flask import Flask, jsonify
import datetime
import random
from utils.logger import get_logs

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Flask App"
        })

@app.route("/health")
def health_check():
    return jsonify({"status": "Healthy", "timestamp": str(datetime.datetime.utcnow())})

@app.route("/info")
def info():
    return "I am from India"

@app.route("/phone")
def phone():
    return "1111222233"

@app.route("/api/users")
def get_users():
    users = [
            {"id":1,"name":"Rahul Raipurkar","role":"DevOps Engineer"},
            {"id":2,"name":"Jack","role":"AI Engineer"}

             ]
    return jsonify(users)

@app.route('/api/metrics')
def get_metrics():
    metrics = {
        "cpu_usage": f"{random.randint(10, 90)}%",
        "memory_usage": f"{random.randint(1024, 8192)} MB",
        "active_containers": random.randint(1, 10),
        "last_updated": str(datetime.datetime.utcnow())
    }
    return jsonify(metrics)

@app.route('/api/logs')
def get_system_logs():
    logs = get_logs()
    return jsonify({"logs": logs})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)




