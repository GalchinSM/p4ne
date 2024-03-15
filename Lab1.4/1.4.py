import ipaddress
import random


class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        super().__init__((random.randint(0x0b000000, 0xdf000000), random.randint(8, 24)), strict=False)

    def get_network_address(self):
        return self.network_address

    def get_network_mask(self):
        return self.netmask


networks_list = []

for i in range(0, 51):
    networks_list.append(IPv4RandomNetwork())

sorted_networks_list = sorted(networks_list, key=lambda x: (x.prefixlen, x.network_address))

for network in sorted_networks_list:
    print(network)
