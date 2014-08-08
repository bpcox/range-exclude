#! /usr/bin/env python3.4

import ipaddress
import math
supernet = False
subnet = False

while not supernet:

	inputRange = input('Input the IP range you would like remove a subrange from: ')
	try:
		supernet =ipaddress.ip_network(inputRange)
	except ValueError:
		print('Invalid input, try again')

while not subnet:

	inputRange = input('Input the IP range you would like to remove: ')
	try:
		subnet = ipaddress.ip_network(inputRange)
	except ValueError:
		print('Invalid input, try again')
	
if (supernet.version == subnet.version):
	result =supernet.address_exclude(subnet)
	for IPrange in result:
		print(IPrange)
else:
	print('Both IP ranges must be of the same type (IPv4 or IPv6)')
