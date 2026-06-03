import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return {
        "total": round(memory.total / (1024 ** 3), 2),
        "used": round(memory.used / (1024 ** 3), 2),
        "percent": memory.percent
    }

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return {
        "total": round(disk.total / (1024 ** 3), 2),
        "used": round(disk.used / (1024 ** 3), 2),
        "percent": disk.percent
    }

if __name__ == "__main__":
    print(f"CPU Usage: {get_cpu_usage()}%")
    
    mem = get_memory_usage()
    print(f"Memory - Total: {mem['total']}GB | Used: {mem['used']}GB | Percent: {mem['percent']}%")
    
    disk = get_disk_usage()
    print(f"Disk - Total: {disk['total']}GB | Used: {disk['used']}GB | Percent: {disk['percent']}%")