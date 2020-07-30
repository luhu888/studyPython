import json
import socket
import struct
from time import sleep

"""
#格式：　　设置颜色开始 ：\033[显示方式;前景色;背景色m#说明：
前景色            背景色           颜色
---------------------------------------
30                40              黑色
31                41              红色
32                42              绿色
33                43              黃色
34                44              蓝色
35                45              紫红色
36                46              青蓝色
37                47              白色
显示方式           意义
-------------------------
0                终端默认设置
1                高亮显示
4                使用下划线
5                闪烁
7                反白显示
8                不可见
 
#例子：
\033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
\033[0m          <!--采用终端默认设置，即取消颜色设置-->
"""
# sk = socket.socket()
# sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 重启不会报错端口被占用
# sk.bind(('127.0.0.1', 9004))  # 申请操作系统的资源
# sk.listen()
# while 1:
#     conn, addr = sk.accept()  # 解包，返回的是一个元组
#     print(conn, addr)
#     while 1:
#         str = input('请输入聊天内容：')
#         conn.send(str.encode('utf-8'))  # conn里存储的是一个客户端和server端的连接信息
#
#         if str == 'q':
#             break
#         msg = conn.recv(1024).decode('utf-8')
#         print(msg)
#     conn.close()  # 挥手断开连接
# sk.close()  # 归还申请操作系统的资源
#
#

# sk = socket.socket()
# sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sk.bind(('127.0.0.1', 9001))
# sk.listen()
# print('服务已开启')
# while 1:
#     conn, address = sk.accept()
#     while 1:
#         send = input('请输入聊天内容：')
#         conn.send(send.encode('utf-8'))
#         if send == 'Q':
#             break
#         msg = conn.recv(1024)
#         print(msg.decode('utf-8'))
#     conn.close()

#
# sk = socket.socket()
# sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sk.bind(('127.0.0.1', 9001))
# sk.listen()
# print('服务启动成功')
# conn, address = sk.accept()
# # sleep(0.1)
# """
# 连续发两条消息，有一定几率会出现粘包现象
# 只会发生在tcp协议中，因为tcp协议多条消息之间没有边界，且有一堆优化的代码
# 发送端：两条消息都很短，发送的间隔时间也很短
# 接收端：多条消息由于没有及时接收，而在接收方的缓存短，堆在一起导致的粘包
# 可以通过设置边界解决此问题
# """
# send = '1234'
# blen = struct.pack('i', len(send.encode('utf-8')))
# conn.send(blen)
# conn.send('1234'.encode('utf-8'))
# conn.send('5555'.encode('utf-8'))
# conn.close()


sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.listen()
conn, address = sk.accept()
str = conn.recv(1024).decode('utf-8')
str1 = json.loads(str)
print(str)
with open('copy.md', mode='wb') as f:
    msg = conn.recv(str1['file_size'])
    f.write(msg)

conn.close()
sk.close()

























