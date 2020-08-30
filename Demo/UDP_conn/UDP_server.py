import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9000))
print('udp服务开启')
msg, adress = sk.recvfrom(1024)
print('\033[0;32;46m' + msg.decode('utf-8')+'\033[0m')
while 1:
    send = input('输入发送内容：').encode('utf-8')
    sk.sendto(send, adress)




