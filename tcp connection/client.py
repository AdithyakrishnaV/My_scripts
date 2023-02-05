#!/usr/bin/python3

import socket

clientsocket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host=socket.gethostbyname()
port=3000

clientsocket.connect(('<IP of server>',port))

message=clientsocket.recv(1024)
clientsocket.close()

#print(message)
print(message.decode('ascii'))