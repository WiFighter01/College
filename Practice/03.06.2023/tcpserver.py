from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 64
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        data2 = ' Привет, это добавочная строка'
        prob = ' '
        if data == '':
            break
        tcpCliSock.send(ctime().encode(encoding='utf-8') + prob.encode(encoding='utf-8') + data + data2.encode(encoding='utf-8'))
    tcpCliSock.close()
tcpSerSock.close()
