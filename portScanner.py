#!/usr/bin/python3
# pip3 install python-nmap    

import nmap

scanner = nmap.PortScanner()

print("This is an IP scanner to find the PORTS")
ip = input("Enter the ip address to scan: \n")

print("The IP you entered is ", ip)

res= input("""\n Select a scan type:
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan \n""")

if (res=='1'):
    print("Nmap version: ",scanner.nmap_version())
    scanner.scan(ip,'1-1024','-v -sS')
    print(scanner.scaninfo())
    print("IP status: ",scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("Open ports: ",scanner[ip]['tcp'].keys())
elif (res=='2'):
    print("Nmap version: ",scanner.nmap_version())
    scanner.scan(ip,'1-1024','-v -sU')
    print(scanner.scaninfo())
    print("IP status: ",scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("Open ports: ",scanner[ip]['udp'].keys())
elif (res=='3'):
    print("Nmap version: ",scanner.nmap_version())
    scanner.scan(ip,'1-1024','-v -sS -sC -sV -A -O')
    print(scanner.scaninfo())
    print("IP status: ",scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("Open ports: ",scanner[ip]['tcp'].keys())
elif res >= '4':
    print("Enter a valid option")