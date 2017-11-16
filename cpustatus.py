import psutil

#status = psutil.cpu_times_percent(interval=1, percpu=False)
#print(status)
#sum = round(100 - status[3],1)
#print("Current active use of CPU: {} %".format(sum))

def cpu_percentage(max_cpu):
    status = psutil.cpu_times_percent(interval=1, percpu=False)
    usage = round(100 - status[3],1)
    if usage > max_cpu:
        return "exceeded"
    else:
        return "ok"
