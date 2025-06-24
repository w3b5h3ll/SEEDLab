## IP Address
Special Addr
Private IP Addresses
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16

Loopback Address
127.0.0.0/8
Commonly used:  127.0.0.1


ip -br address 的核心功能是以简洁格式显示所有网络接口的 IPv4/IPv6 地址及相关状态，避免默认输出的冗余信息，适合快速检查接口的网络配置。

关键参数解析
ip：Linux 网络配置工具，用于管理网络接口、地址、路由等。
-br（--brief）：简洁模式（brief 的缩写），过滤非必要细节，仅保留关键信息。
address：子命令，用于操作或查看网络接口的 IP 地址。

```bash
┌──(kali㉿kali)-[~/Works/network_security/09]
└─$ ip -br address
lo               UNKNOWN        127.0.0.1/8 ::1/128 
wlan0            UP             192.168.100.241/24 240e:46d:6620:eb6:bde4:1bdb:2c30:4cf7/64 2408:840d:6a20:3c24:a142:4017:d6e5:fba4/64 fe80::fc04:a95f:57cd:7da5/64 

```
手动设置IP地址
```bash
sudo ip addr add 192.x.x.x/x dev enp0s3
```
自动设置IP
- DHCP

Get IP Address for Host Name: DNS
```bash
┌──(kali㉿kali)-[~]
└─$ dig baidu.com

; <<>> DiG 9.20.4-4-Debian <<>> baidu.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 65043
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;baidu.com.                     IN      A

;; ANSWER SECTION:
baidu.com.              573     IN      A       182.61.244.181
baidu.com.              573     IN      A       182.61.201.211

;; Query time: 8 msec
;; SERVER: 192.168.100.90#53(192.168.100.90) (UDP)
;; WHEN: Tue Jun 24 03:12:00 EDT 2025
;; MSG SIZE  rcvd: 59

```

## UDP Client && Server
```bash
nc -luv 9000
```
nc -luv 9000 的作用是：
在本地的 9000 端口启动一个 UDP 监听器，等待接收来自其他主机的 UDP 数据报，并以详细模式输出接收到的数据和客户端信息。

```bash
┌──(kali㉿kali)-[~/Works/SEEDLabs/network_security/09]
└─$ python ./udp_client.py 
已发送数据：Hello, UDP from Python! 到 ('127.0.0.1', 9000)

┌──(kali㉿kali)-[~]
└─$ nc -luvp 9000
listening on [any] 9000 ...
connect to [127.0.0.1] from localhost [127.0.0.1] 53847
Hello, UDP from Python!


```

## How Packets Are Received?
Port >> Transport Layer >> Network Layer(Routing) >> MAC Layer

Routing Table
```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ ip route show        
default via 192.168.100.90 dev wlan0 proto dhcp src 192.168.100.241 metric 600 
192.168.100.0/24 dev wlan0 proto kernel scope link src 192.168.100.241 metric 600 
```
```bash
default via 10.9.0.1 dev eth0
10.9.0.0/24 dev eth0 proto kernel scope link src 10.9.0.11
192.168.60.0/24 dev eth1 proto kernel scope link src 192.168.60.11
```
默认路由：所有未匹配其他规则的数据包将通过eth0接口发送到网关10.9.0.1
本地网络1：10.9.0.0/24网段通过eth0接口直接连接，本地源IP为10.9.0.11
本地网络2：192.168.60.0/24网段通过eth1接口直接连接，本地源IP为192.168.60.11

Packet Sending Tools
netcat:
- nc <ip> <port>
- nc -u <ip> <port>


