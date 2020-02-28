"""
1
"""

from socket import *

# 全局变量
ADDR = ('0.0.0.0',8888)

# 应用于存储用户 {name:address}
user={}

# 处理进入聊天室请求
def do_login(s,name,addr):
    if name in user:
        s.sendto(b"FAIL",addr)
        return
    else:
        s.sendto(b"OK", addr)

    # 通知其他人
    msg = "欢迎 '%s' 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name] = addr # 字典中加入一项

# 基本结构 （接收请求，分配任务）
def main():
    # udp服务端套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    # 循环接收请求
    while True:
        data,addr = s.recvfrom(1024)
        tmp = data.decode().split(' ') # 请求内容做简单的解析
        print("接收到的请求:", tmp)
        # data --> 接收到的请求
        if tmp[0] == 'L':
            do_login(s,tmp[1],addr)
        elif tmp[0] == 'C':
            pass
        elif tmp[0] == 'Q':
            pass

if __name__ == '__main__':
    main()
