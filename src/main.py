import time
import threading
from logger import log_metrics
from api import app

def run_api():
    app.run(host='127.0.0.1', port=5000)

if __name__ == "__main__":
    print("SysGuard started...")
    
    api_thread = threading.Thread(target=run_api)
    api_thread.daemon = True
    api_thread.start()
    
    while True:
        log_metrics()
        time.sleep(60)