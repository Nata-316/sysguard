import time
import threading
from datetime import datetime, timedelta
from logger import log_metrics
from anomaly import load_data, train_model, detect
from emailer import send_alert
from api import app

def run_api():
    app.run(host='127.0.0.1', port=5000)

if __name__ == "__main__":
    print("SysGuard started...")

    data = load_data()
    if len(data) >= 10:
        model = train_model(data)
        print(f"ML model trained on {len(data)} readings")
    else:
        model = None
        print("Not enough data to train model yet")


    retrain_counter = 0


    api_thread = threading.Thread(target=run_api)
    api_thread.daemon = True
    api_thread.start()

    last_alert_time = None

    while True:
        metrics = log_metrics()

        if model:
            if detect(model, metrics):
                now = datetime.now()
                if last_alert_time is None or (now - last_alert_time) > timedelta(minutes=30):
                    print("Anomaly detected! Sending alert...")
                    send_alert(
                        "ANOMALY: SysGuard ML Alert",
                        f"Anomalous system behavior detected: {metrics}"
                    )
                    last_alert_time = now

        retrain_counter += 1
        if retrain_counter >= 60:
            data = load_data()
            if len(data) >= 10:
                model = train_model(data)
                print(f"ML model retrained on {len(data)} readings")
            retrain_counter = 0
        time.sleep(60)