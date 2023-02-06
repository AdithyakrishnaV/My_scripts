#!/usr/bin/python3

import socket

def PortScan(ip,port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host=ip
    s.settimeout(6)
    if s.connect_ex((host,int(port))):
        print("Port is closed")
    else:
        print("Port is open")
    
def main():
    ip=input("Enter the ip address:  ")
    port=str(input("Enter the port to scan:  "))
    PortScan(ip,port)

main()
