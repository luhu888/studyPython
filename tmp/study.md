#### 一、编码ASCII码 &&gbk && unicode
8bit = 1byte   8位等于1个字节
1024 byte = 1kb
1024 kb = 1M
1024M = 1G
1024G = 1T
ASCII码：只包含英文字母，数字，特殊符号
一个字符占用一个字节
gbk码：包含英文字母，数字，特殊符号和中文
一个中文字符占两个字节，其他占一个字节
unicode码（万国码）：所有国家的字符都包含
一个字符都占用两个字节
utf-8：unicode的升级，最少用8bit1个字节表示一个字符，英文字符占用一个字节，欧洲字符占用两个字符，中文字符占用三个字节
数据在内存中全部是以Unicode编码的，但是当数据用于网络传输或存到硬盘中，必须是以非Unicode编码（gbk等）

网络七层协议：应用层，表示层，会话层，传输层，网络层，数据链路层，物理层
被简化成osi五层协议：
应用层，  python代码
传输层，  port   四层交换机，四层路由器
网络层，  ipv4，ipv6 路由器 三层交换机
数据链路层，mac，arp(地址解析协议)， 网卡，二层交换机
物理层   电信号

tcp协议 ：需要提前建立链接，才能通信（打电话），会占用连接，可靠消息不会丢失，实时性高（视频下载）
udp协议 ：不需要建立连接就可以通信（发短信），不够可靠（在线视频）

tcp建立连接，三次握手，四次挥手（全双工通信（双向都可以通信））
三次握手：1.客户端发起请求连接SYN报文，2.服务端同意ACK确认并请求连接客户端SYN报文，3.客户端同意ACK确认
四次挥手：1.一方发起断开请求FIN字节，2.另一方同意，另一方可能有些数据没接收完，只断开单向连接，3.数据接受完，另一方发起断开请求FIN字节，4.一方同意


