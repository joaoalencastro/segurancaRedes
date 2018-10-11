#!/usr/bin/env python

#########################################
#	Autor: João Alencastro		#
#########################################

import nmap, os

nm = nmap.PortScanner() # instantiate nmap.PortScanner object

ip_list = ['127.0.0.1']
ports = '21,443,8000'

for ip in ip_list:
	nm.scan(ip, arguments="-O -p "+ports)
	print('------------------------------------------')
	print('\nFor IP address: ', ip)

	#procurando SO remoto
	if not nm[ip]['osmatch']:
		pass
	else:
		print(nm[ip]['osmatch'][0]['name'])

	if not nm[ip].all_tcp():
		#lista de portas TCP esta vazia
		print('There are no TCP open ports')
	else:
		#para todas as portas TCP da lista
		print('TCP open ports are:\n')
		for port in ports.split(','):
			if nm[ip]['tcp'][int(port)]['state'] != 'open':
				pass
			else:
				print( '[+] Port', port, ' is open')
				print('---------------------')

	

	if not nm[ip].all_udp():
		#lista de portas UDP esta vazia
		print('There are no UDP open ports')
	else:
		#para todas as portas UDP da lista
		print('UDP open ports are:\n')
		for port in ports.split(','):
			if nm[ip]['udp'][int(port)]['state'] != 'open':
				pass
			else:
				print( '[+] Port', port, ' is open')
				print('---------------------')
		
