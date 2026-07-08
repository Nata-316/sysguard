from monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_network_usage
from alerts import check_alerts
import logging

logging.basicConfig(
    filename = 'logs/sysguard.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def log_metrics():

    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    net = get_network_usage()

    breaches = check_alerts(cpu, memory, disk, net)

    # TODO: log each metric — WARNING if it appears in `breaches`,
    # INFO otherwise. Think about how you'll check "is this metric in
    # the breach list" without an O(n) scan of `breaches` per metric.

if __name__ == "__main__":
    log_metrics()
