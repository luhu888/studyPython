import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
server = ('127.0.0.1', 9000)
while 1:
    send = input('输入回复内容：').encode('utf-8')
    sk.sendto(send, server)
    msg = sk.recv(1024).decode('utf-8')
    print(msg)
    if msg == 'q':
        break




