import socketserver
class myServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        addr =self.client_address
        print("客户端地址："+str(addr))
        while True:
            recv_data = conn.recv(1024)
            if recv_data.decode("utf-8") == "exit":
                print("say baibai!")
                conn.close()
                break
            else:
                print("收到的内容:" + recv_data.decode("utf-8"))
            send_data = input(">>>")
            conn.sendall(send_data.encode("utf-8"))
        conn.close()
if __name__== "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1",8899),myServer)
    server.serve_forever()