from pysnmp.hlapi import *

engine = SnmpEngine()
comm_data = CommunityData('public', mpModel=0)
transport = UdpTransportTarget(('10.31.70.209', 161))
context_data = ContextData()
snmp_version = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_interfaces = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result = nextCmd(engine, comm_data, transport, context_data, ObjectType(snmp_interfaces), lexicographicMode=False)
result2 = getCmd(engine, comm_data, transport, context_data, ObjectType(snmp_version))

for r in result:
    for r2 in r[3]:
        print(str(r2).split(' = ')[1])

for r in result2:
    for r2 in r[3]:
        print(r2)
