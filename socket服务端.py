from socket import *
HOST = '0.0.0.0'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)
tcpsersock = socket(AF_INET,SOCK_STREAM)
tcpsersock.bind(ADDR)
tcpsersock.listen(5)
print('等到客户端连接：')

tcpclisock,addr = tcpsersock.accept()
print('连接来自：',addr)
while True:
    data = tcpclisock.recv(BUFSIZ)
    if not data:
        tcpclisock.close()
        break
    rstr = data.decode()
    print(rstr)
    tcpclisock.sendall(f'**{rstr}'.encode())
tcpsersock.close()
