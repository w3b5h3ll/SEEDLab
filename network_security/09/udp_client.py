#!/usr/bin/python
import socket
# 创建 UDP Socket（AF_INET 表示 IPv4，SOCK_DGRAM 表示 UDP）
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 要发送的数据（字符串需编码为 bytes）
message = "Hello, UDP from Python!"
data = message.encode("utf-8")  # 编码为 UTF-8 字节流

# 目标地址（替换为接收端的 IP 和端口）
target_addr = ("127.0.0.1", 9000)  # 本地测试用回环地址

# 发送数据
udp_socket.sendto(data, target_addr)
print(f"已发送数据：{message} 到 {target_addr}")

udp_socket.close()
