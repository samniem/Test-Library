import psutil

#checks if a mount partition uses more than max allowed space
def partition_usage(mount,max_disk_use):
    usage = psutil.disk_usage(mount)
    if usage[3] > max_disk_use:
        return False
    else:
        return True
