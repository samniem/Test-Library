import psutil

status = psutil.cpu_times_percent(interval=1, percpu=False)
print(status)
sum = round(100 - status[3],1)
print("Current active use of CPU: {} %".format(sum))
