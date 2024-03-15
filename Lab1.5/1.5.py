import glob
import re

ip_list = []

dir_name = 'config_files'
file_list = glob.glob(f'{dir_name}\\*.log')

for file_name in file_list:
    with open(file_name) as file:
        file_lines = file.readlines()
        for line in file_lines:
            if 'ip address' in line:
                ip_and_mask_str = ' '.join(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line))
                if ip_and_mask_str:
                    ip_list.append(ip_and_mask_str)

[print(item) for item in list(set(ip_list))]
