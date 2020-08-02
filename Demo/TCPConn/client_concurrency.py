import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9001))
while 1:
    for i in range(1, 10):
        sk.send(str(i).encode('utf-8'))
    content = sk.recv(1).decode('utf-8')
    print(content)
