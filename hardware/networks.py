import psutil

#checking if a network with a name exists
def network_exists(network_name):
    networks = psutil.net_if_addrs()
    if network_name in networks:
        return True
    else:
        return False
