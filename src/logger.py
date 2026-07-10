import json
import logging
from monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_network_usage
from alerts import check_alerts

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(log_data)

logger = logging.getLogger("sysguard")
logger.setLevel(logging.INFO)

handler = logging.FileHandler('/home/natty/sysguard/logs/sysguard.log')
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)

def log_metrics():
    cpu = get_cpu_usage()
    logger.info(f"CPU Usage: {cpu}%")

    memory = get_memory_usage()
    logger.info(f"Memory - Total: {memory['total']}GB | Used: {memory['used']}GB | Percent: {memory['percent']}%")

    disk = get_disk_usage()
    logger.info(f"Disk - Total: {disk['total']}GB | Used: {disk['used']}GB | Percent: {disk['percent']}%")

    net = get_network_usage()
    logger.info(f"Network - Sent: {net['bytes_sent']}MB | Received: {net['bytes_recv']}MB")

    check_alerts()

if __name__ == "__main__":
    log_metrics()