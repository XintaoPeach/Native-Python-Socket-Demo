"""
演示Socket服务端开发
"""
import socket

# 创建Socket对象
socket_server = socket.socket()

# 绑定ip地址和端口
socket_server.bind(("localhost", 8888))

# 监听端口: 整数参数表示接受链接的对象
socket_server.listen(1)

# 等待客户端链接: 返回二元元组(链接对象, 客户端地址信息)，accept是阻塞方法，即运行到当前行不会再往下运行
# result = socket_server.accept()
# conn = result[0]        # 客户端和服务端的链接对象
# address = result[1]     # 客户端的地址信息
conn, address = socket_server.accept()
print(f'接收到了客户端的链接, 客户端的信息为: {address}')

while True:
    # 接受客户端信息, 这里使用的是客户端和服务端的本次连接对象，而不是socker_server对象
    # recv接受的参数是缓冲区大小，一般为1024即可
    # recv方法的返回值是一个字节数组，也就是bytes对象，不是字符串，可以通过decode方法UTF-8编码，将字节数组转换为字符串对象
    data = conn.recv(1024).decode("UTF-8")
    print(f"客户端发送的消息为: {data}")
    msg = input("请输入你要回复的对象：")
    if msg == 'exit':
        break
    # 发送回复消息
    conn.send(msg.encode("UTF-8"))

# 关闭链接
conn.close()
socket_server.close()
