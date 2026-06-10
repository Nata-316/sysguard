from monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_network_usage

def check_alerts():

    cpu_usage = get_cpu_usage()
    if cpu_usage > 80:
        print(f"WARNING: CPU usage is high at {cpu_usage}%")

    memory_usage = get_memory_usage()
    if memory_usage['percent'] > 1:
        print(f"WARNING: Memory usage is high at {memory_usage['percent']}%")

    disk_usage = get_disk_usage()
    if disk_usage['percent'] > 85:
        print(f"WARNING: Disk usage is high at {disk_usage['percent']}%")
    
    network_usage = get_network_usage()
    if network_usage['bytes_sent'] > 1000 or network_usage['bytes_recv'] > 5000:
        print(f"WARNING: High network usage - Bytes Sent: {network_usage['bytes_sent']}MB | Bytes Received: {network_usage['bytes_recv']}MB")

if __name__ == "__main__":
    check_alerts()