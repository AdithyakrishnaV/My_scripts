#!/usr/bin/python3

#Banner grabbing is a technique used to gain information 
#about a computer system on a network and the services 
#running on its open ports.

import socket 

def grab(ip,port):
    s=socket.socket()
    s.connect((ip,int(port)))
    s.settimeout(6)
    print(str(s.recv(1024)).strip('b'))

def main():
    ip = input("Enter the ip address: ")
    port= str(input("Enter the port: "))
    grab(ip,port)

main()

