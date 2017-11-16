import psutil

def network_exists(network_name):
    networks = psutil.net_if_addrs()
    if network_name in networks:
        return True
    else:
        return False
