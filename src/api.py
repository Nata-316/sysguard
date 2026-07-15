from flask import Flask, jsonify
from monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_network_usage

app = Flask(__name__)

@app.route('/metrics')
def get_metrics():
    return jsonify({
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "network": get_network_usage()
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)