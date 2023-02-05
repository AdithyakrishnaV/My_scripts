#!/usr/bin/python3

import socket;
# AF_INET is the Internet address family for IPv4. 
# SOCK_STREAM is the socket type for TCP

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host -> ip of the server
#host=socket.gethostbyname()
port=3000

serversocket.bind(('<IP of server>', port))

serversocket.listen(2)

while True:
    clientsocket, address=serversocket.accept()

    print("connecting received from from %s "% str(address))

    string='Hello!!! Thank you for connecting to the server'+'\r \n'
    # convert string to UTF-8 encoded bytes
    message=string.encode('utf-8')
    # pass the encoded string to the function
    clientsocket.send(message)

    clientsocket.close()