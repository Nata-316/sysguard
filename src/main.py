import time
import threading
from logger import log_metrics
from api import app
from anomaly import load_data, train_model, detect
from emailer import send_alert

def run_api():
    app.run(host='127.0.0.1', port=5000)

if __name__ == "__main__":
    print("SysGuard started...")
    
    data = load_data()
    print(f"Loaded {len(data)} readings")
    if len(data) >= 10:
        model = train_model(data)
        print(f"ML model trained on {len(data)} readings")
    else:
        model = None
        print("Not enough data yet — need at least 10 readings")
        

    api_thread = threading.Thread(target=run_api)
    api_thread.daemon = True
    api_thread.start()
    
    while True:
        metrics = log_metrics()
        if model:
            if detect(model, metrics):
                print("Anomaly detected! Sending alert...")
                send_alert("SysGuard Alert", f"Anomaly detected in system metrics: {metrics}")
        time.sleep(60)

