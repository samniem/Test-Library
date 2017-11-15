import subprocess
import unittest

service1="dnsmasq"
service2="nfs-kernel-server"
service3="sshd"
service4="vim"

def status(name):
    out=""
    process = subprocess.Popen(["ps", "-a"], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = process.communicate()
    if (name in out):
        return name
    else:
        return "failure"

class TestStatus(unittest.TestCase):

    def test_status(self):
        self.assertEqual(status(service1),service1)
        self.assertEqual(status(service2),service2)
        self.assertEqual(status(service3),service3)
        self.assertEqual(status(service4),service4)

if __name__ == '__main__':
    unittest.main()
