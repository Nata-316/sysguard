from monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_network_usage
import state
def check_alerts():

    cpu_usage = get_cpu_usage()
    if cpu_usage > 85:
        state.cpu_alert_count += 1
        if state.cpu_alert_count >= 3:
            print(f"CRITICAL: CPU has been high for {state.cpu_alert_count} consecutive checks at {cpu_usage}%")
        else:
            print(f"WARNING: CPU usage is high at {cpu_usage}%")
    else:
        state.cpu_alert_count = 0

    memory_usage = get_memory_usage()
    if memory_usage['percent'] > 1:
        state.memory_alert_count += 1
        if state.memory_alert_count >= 3:
            print(f"CRITICAL: Memory has been high for {state.memory_alert_count} consecutive checks at {memory_usage['percent']}%")
        else:       
            print(f"WARNING: Memory usage is high at {memory_usage['percent']}%")
    else:
        state.memory_alert_count = 0

    disk_usage = get_disk_usage()
    if disk_usage['percent'] > 85:
        state.disk_alert_count += 1
        if state.disk_alert_count >= 3:
            print(f"CRITICAL: Disk has been high for {state.disk_alert_count} consecutive checks at {disk_usage['percent']}%")
        else:
            print(f"WARNING: Disk usage is high at {disk_usage['percent']}%")
    else:
        state.disk_alert_count = 0

    network_usage = get_network_usage()
    if network_usage['bytes_sent'] > 1000 or network_usage['bytes_recv'] > 5000:
        print(f"WARNING: High network usage - Sent: {network_usage['bytes_sent']}MB | Received: {network_usage['bytes_recv']}MB")

if __name__ == "__main__":
    check_alerts() 