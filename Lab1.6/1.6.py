import ipaddress
import glob
import re


def find_interface(target_line: str):
    if m := re.match(
            r' ip address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
            target_line):
        return ipaddress.IPv4Interface((m.group(1), m.group(2)))


interface_list = []

dir_name = 'config_files'
file_list = glob.glob(f'{dir_name}\\*.log')

for file_path in file_list:
    with open(file_path) as file:
        file_lines = file.readlines()
        for line in file_lines:
            if interface := (find_interface(line)):
                interface_list.append(interface)

for interface in interface_list:
    print(interface)
