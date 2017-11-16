import psutil
result = psutil.net_if_addrs()
typ = type(result)
print(result.keys())
if "enp2s0" in result:
    print(result["enp2s0"])
#nplist = result["enp2s0"]
#print(enplist)
#print(enplist[0])
