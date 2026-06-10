from monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_network_usage
import logging

logging.basicConfig(
    filename = 'logs/sysguard.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def log_metrics():
    
    cpu = get_cpu_usage()
    if cpu > 85:
        logging.warning(f"High CPU usage detected: {cpu}%")
    else:
        logging.info(f"CPU Usage: {cpu}%")
    
    memory = get_memory_usage()
    if memory['percent'] > 85:
        logging.warning(f"High Memory usage detected: {memory['percent']}%")
    else:
        logging.info(f"Memory - Total: {memory['total']}GB | Used: {memory['used']}GB | Percent: {memory['percent']}%")
    
    disk = get_disk_usage()
    if disk['percent'] > 85:
        logging.warning(f"High Disk usage detected: {disk['percent']}%")
    else:
        logging.info(f"Disk - Total: {disk['total']}GB | Used: {disk['used']}GB | Percent: {disk['percent']}%")
    
    net = get_network_usage()
    logging.info(f"Network - Bytes Sent: {net['bytes_sent']}MB | Bytes Received: {net['bytes_recv']}MB")

if __name__ == "__main__":
    log_metrics()