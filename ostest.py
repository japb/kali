#!/usr/bin/env python

from scapy.all import *

ans = raw_input("Enter target IP : ")

ip = IP()
ping = ICMP()
ip.dst = ans
reply = sr1(ip/ping)
if reply.ttl < 65:
	os = "linux"
else:
	os = "windows"

print "OS is " + os
