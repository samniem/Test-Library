import psutil

partitions = psutil.disk_partitions()
usage = psutil.disk_usage('/')
print(partitions)
print("root partition / disk usage: {}".format(usage))
