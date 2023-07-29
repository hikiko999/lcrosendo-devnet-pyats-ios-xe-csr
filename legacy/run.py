from pyats.topology import loader

testbed = loader.load('ios_testbed.yml')

testbed.devices
ios_1 = testbed.devices['csr1000v-1']

ios_1.connect()

print(ios_1.execute('show version'))
ios_1.configure('''
    interface Loopback79
        ip address 20.30.40.50 255.255.255.0
        description PYATS'D INTERFACE
''')
print(ios_1.execute('show ip int brief'))