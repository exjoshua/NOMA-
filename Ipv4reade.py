#!/usr/lib/python3.4
import socket
import struct
import binascii
sock_raw = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)
while True:
    data = sock_raw.recvfrom(65535)
    #print(type(data))
    #print(data)
    #dataunpack = struct.unpack(data)
    #print(dataunpack)
    ipHeader = data[0][0:20]
    tcpHeader = data[0][20:40]

    ip_hdr = struct.unpack("BcHHHccH4s4s",ipHeader)
    tcp_hdr = struct.unpack("!HHIIHHHH",tcpHeader)#TCPanalyzier
    print(ip_hdr)
    shift_ip = ip_hdr[0]
    print('ip首部长度为:',(shift_ip & 0x0f)*4)
    print(tcp_hdr)
    shift_tcp = tcp_hdr[4]
    print('首部长度为:', ((shift_tcp & 0xf000)>>12)*4)








