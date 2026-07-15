import json
import logging

from sklearn import metrics
from monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_network_usage
from alerts import check_alerts

class JSONFormatter(logging.Formatter):
    def format(self, record):
        message = record.getMessage()
        try:
            data = json.loads(message)
        except (json.JSONDecodeError, TypeError):
            data = {"message": message}
        
        log_data = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            **data
        }
        return json.dumps(log_data)

logger = logging.getLogger("sysguard")
logger.setLevel(logging.INFO)

handler = logging.FileHandler('/home/natty/sysguard/logs/sysguard.log')
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)

def log_metrics():
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    net = get_network_usage()

    metrics = {
        "cpu": cpu,
        "memory_percent": memory['percent'],
        "disk_percent": disk['percent'],
        "network_sent": net['bytes_sent'],
        "network_recv": net['bytes_recv']
    }

    logger.info(json.dumps(metrics))
    check_alerts()
    print(f"Debug metrics: {metrics}")
    return metrics

if __name__ == "__main__":
    log_metrics()