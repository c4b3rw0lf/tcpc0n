#!/usr/bin/env python

from pyfiglet import Figlet
f = Figlet(font='slant')
print f.renderText('tcpc0n')

print '##### TCP Client #####'
print '##### By c4b3rw0lf #####'

import socket 

target_host = "127.0.0.1" 
target_port = 80

# Create socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect tcpc0n to target
client.connect((target_host,target_port))

# Send data to target
client.send("HEAD / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")

# Receive data from target
response = client.recv(4096)

print response




