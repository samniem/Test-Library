import subprocess

f = open("testhelloworld.py", "a")
f.write('print("hello world")')
#f.write('subprocess.Popen([spawn failure])')
f.close()

pros = subprocess.Popen(["python3", "testhelloworld.py"], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
result = pros.communicate()[0]

print(result)
pros2 = subprocess.Popen(["rm", "testhelloworld.py"], stderr=subprocess.STDOUT)
