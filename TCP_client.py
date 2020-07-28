import socket
import struct

"""

socket.socket(socket_family,socket_type,protocal=0)
 socket_family 可以是 AF_UNIX 或 AF_INET。socket_type 可以是 SOCK_STREAM 或 SOCK_DGRAM。protocol 一般不填,默认值为 0。

 获取tcp/ip套接字
tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

获取udp/ip套接字
udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

由于 socket 模块中有太多的属性。我们在这里破例使用了'from module import *'语句。使用 'from socket import *',我们就把 socket 模块里的所有属性都带到我们的命名空间里了,这样能 大幅减短我们的代码。
例如tcpSock = socket(AF_INET, SOCK_STREAM)
服务端套接字函数
s.bind()    绑定(主机,端口号)到套接字
s.listen()  开始TCP监听
s.accept()  被动接受TCP客户的连接,(阻塞式)等待连接的到来

客户端套接字函数
s.connect()     主动初始化TCP服务器连接
s.connect_ex()  connect()函数的扩展版本,出错时返回出错码,而不是抛出异常

公共用途的套接字函数
s.recv()            接收TCP数据
s.send()            发送TCP数据(send在待发送数据量大于己端缓存区剩余空间时,数据丢失,不会发完)
s.sendall()         发送完整的TCP数据(本质就是循环调用send,sendall在待发送数据量大于己端缓存区剩余空间时,数据不丢失,循环调用send直到发完)
s.recvfrom()        接收UDP数据
s.sendto()          发送UDP数据
s.getpeername()     连接到当前套接字的远端的地址
s.getsockname()     当前套接字的地址
s.getsockopt()      返回指定套接字的参数
s.setsockopt()      设置指定套接字的参数
s.close()           关闭套接字

面向锁的套接字方法
s.setblocking()     设置套接字的阻塞与非阻塞模式
s.settimeout()      设置阻塞套接字操作的超时时间
s.gettimeout()      得到阻塞套接字操作的超时时间

面向文件的套接字的函数
s.fileno()          套接字的文件描述符
s.makefile()        创建一个与该套接字相关的文件
"""
# sk = socket.socket()
# sk.connect(('127.0.0.1', 9004))   # 申请操作系统的资源
# while 1:
#     msg = sk.recv(1024).decode('utf-8')
#     print(msg)
#     send = input('请输入聊天内容：')
#     sk.send(send.encode('utf-8'))
#     if send == 'q':
#         break
#
# sk.close()  # 归还申请的操作系统的资源


# sk = socket.socket()
# sk.connect(('127.0.0.1', 9001))
# while 1:
#     msg = sk.recv(1024)
#     print('\033[0;31;40m'+msg.decode('utf-8')+'\033[0m')
#     send = input('请输入聊天内容：')
#     sk.send(send.encode('utf-8'))
#     if send == 'Q':
#         break
#
# sk.close()

sk = socket.socket()
sk.connect(('127.0.0.1', 9001))
print('连接服务器成功')
lenth = sk.recv(4)   # 接收到的是元组
lenth1 = struct.unpack('i', lenth)[0]
msg1 = sk.recv(lenth1)
print('\033[0;31;40m' + msg1.decode('utf-8') + '\033[0m')
msg2 = sk.recv(1024)
print(msg2.decode('utf-8'))
sk.close()



























