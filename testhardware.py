import unittest
import cpustatus
import diskstatus
import memorystatus
import networks

#Basic testing for CPU, memory, disk space and network
max_cpu = 30.0          #max cpu usage in %
network_name = "enp2s0" #check if network with this name exists
max_memory = 30.0       #max memory utilization
mount1 = "/"             #check disk use for mount1 & mount2
mount2 = "/home"
max_disk_use = 80.0

class TestHardware(unittest.TestCase):

    def test_cpu_util(self):
        self.assertEqual(cpustatus.cpu_percentage(max_cpu),"ok")

    def test_network(self):
        self.assertEqual(networks.network_exists(network_name),True)

    def test_disks(self):
        self.assertEqual(diskstatus.partition_usage(mount1,max_disk_use), True)
        self.assertEqual(diskstatus.partition_usage(mount2,max_disk_use), True)

    def test_memory(self):
        self.assertEqual(memorystatus.virtual_memory_percentage(max_memory),"ok")

if __name__ == '__main__':
    unittest.main()
