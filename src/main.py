import time
from logger import log_metrics

if __name__ == "__main__":
    print("sysGuard started...")
    while True:
        log_metrics()
        time.sleep(60) 
    