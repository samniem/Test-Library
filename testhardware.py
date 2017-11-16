import unittest
import cpustatus
#import diskstatus
#import memorystatus

max_cpu = 30.0
network_name = "enp2s0"
max_memory = 30.0
mount1 = "/"
mount2 = "/home"

class TestHardware(unittest.TestCase):

    def test_cpu_util(self):
        self.assertEqual(cpustatus.cpu_percentage(max_cpu),"ok")
    def test_network(self):
        pass
    def test_disks(self):
        pass
    def test_memory(self):
        pass

if __name__ == '__main__':
    unittest.main()
