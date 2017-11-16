import psutil

#checks virtual memory use status
def virtual_memory_percentage(max_memory):
    status = psutil.virtual_memory()
    value = status[2]
    if value > max_memory:
        return "exceeded"
    else:
        return "ok"

def swap_memory_percentage():
    pass
