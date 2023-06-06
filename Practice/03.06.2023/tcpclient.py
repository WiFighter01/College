#!/usr/bin/env python
from socket import *

HOST = '127.0.0.1'  # or 'localhost'
PORT = 21567
BUFSIZE = 64
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    while True:
        data = input('Задайте строку для отправки: ')
        if not data:
            break
        tcpCliSock.send(data.encode(encoding='utf-8'))
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        print(data.decode('utf-8'))
tcpCliSock.close()
