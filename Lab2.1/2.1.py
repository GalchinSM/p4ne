import re
import time
import paramiko
import requests

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_connection.connect('10.31.70.209',
                       username='restapi',
                       password='j0sg1280-7@',
                       look_for_keys=False,
                       allow_agent=False)
session = ssh_connection.invoke_shell()

session.send(b'terminal len 0\n')
time.sleep(0.1)
session.send(b'show interface\n')
time.sleep(0.1)
output = session.recv(50000)

interface_list = []
for line in output.decode().split('\n'):
    if m := re.match('(.*) is.*, line protocol is.*', line):
        interface_list.append(f'Interface: {m.group(1)}')
    if m := re.match('(.*) packets output, (.*) bytes,', line):
        interface_list.append(f'Packets: {m.group(1).strip()} Bytes: {m.group(2).strip()}')

for item in interface_list:
    print(item)

######################################################################################################

headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

r = requests.get('https://10.31.70.209' + '/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces',
                 auth=("restapi", "j0sg1280-7@"),
                 headers=headers,
                 verify=False)

interface_list = []
output_list = r.json()['Cisco-IOS-XE-interfaces-oper:interfaces']['interface']

for interface in output_list:
    interface_list.append(
        f"Interface: {interface['name']}\n"
        f"Packets: {interface['v4-protocol-stats']['out-pkts']}"
        f"Bytes: {interface['v4-protocol-stats']['out-octets']}")

for item in interface_list:
    print(item)