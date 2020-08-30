import socketserver
from time import sleep


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        """
        实现并发的socket TCP
        :return:
        """
        conn = self.request
        while 1:
            try:
                content = conn.recv(1024).decode('utf-8')
                conn.send(content.upper().encode('utf-8'))
                sleep(0.5)
            except ConnectionResetError:
                break


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9002), MyServer)
print('服务启动成功')
server.serve_forever()

