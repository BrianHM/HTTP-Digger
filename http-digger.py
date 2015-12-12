#!/usr/bin/python
# HTTP Digger - Scanning HTTP Banner and Methods
# Written by Brian HM (Gr3x)

import socket
import sys

script_name = sys.argv[0]

if len(sys.argv) != 2:
	print "\n[+] HTTP Digger - Scanning HTTP Banner and Methods"
	print "[+] Written by Brian HM (Gr3x)"
	print "[+] Usage: %s <IP Address>\n" % script_name
	sys.exit()

try:
	print "\n[+] HTTP Digger - Scanning HTTP Banner and Methods"
	print "[+] Written by Brian HM (Gr3x)"
	print "[+] Make sure destination port is open and not blocked by firewall!!!"
	print "[+] Target: %s\n" % sys.argv[1]
	
	# Creating TCP Connection...
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connecting to host on port 80...
	s.connect((sys.argv[1], 80))
	
	# Sending HTTP OPTIONS Request to Server...
	s.sendall("OPTIONS / HTTP/1.0\r\n\r\n")
	result = s.recv(4096)
	print result
	s.close()

except socket.gaierror, err:
	print "[-] Whoops!!! We have some issue!!!\n\n" ,sys.argv[1] ,err
	print
	sys.exit()
