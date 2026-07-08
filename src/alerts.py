from monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_network_usage
import config


def check_alerts(cpu, memory, disk, network):
    """
    Compare current metric readings against the thresholds in config.py
    and return a list of breaches.

    Each breach should describe what was breached and by how much, e.g.:
        {"metric": "cpu", "value": 92.1, "threshold": config.CPU_WARNING_THRESHOLD}

    Pure function: no printing, no logging, no side effects. logger.py
    (and later, an email/REST layer) consume this list and decide what
    to do with it — this function should not care who's calling it.
    """
    breaches = []

    # TODO: compare cpu/memory/disk/network against config thresholds
    # and append a breach dict for each one that's over.

    return breaches


if __name__ == "__main__":
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    network = get_network_usage()

    for breach in check_alerts(cpu, memory, disk, network):
        print(f"WARNING: {breach}")
