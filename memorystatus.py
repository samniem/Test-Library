import psutil

out = psutil.virtual_memory()
print(out)
if out[2] > 25:
    print("too large usage")
else:
    print("memory usage ok")

