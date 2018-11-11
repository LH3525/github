from socket import *
HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)
#指明协议
tcpclisock = socket(AF_INET,SOCK_STREAM)#AF_INET表示IP_4协议，SOCK_STREAM表示tcp协议
tcpclisock.connect(ADDR)
while True:
    data = input('>>')
    if not data:
        break
    tcpclisock.send(data.encode())
    data = tcpclisock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode())
tcpclisock.close()
