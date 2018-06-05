#!/usr/lib/python3.4
#-*-coding:utf-8-*-

import socket, struct

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))

while True:
    data = s.recvfrom(65535)
    ethheader = data[0][14]
    ipHeader = data[0][14:34]
    ip_hdr = struct.unpack("!BcHHHccH4s4s", ipHeader)  # 按格式展开IP头

    if ip_hdr[6] == b'\x11': #如果是UDP格式
        udpHeader = data[0][34:42]
        udp_hdr = struct.unpack("!HHHH", udpHeader)
        print(ip_hdr)
        print('src ip:' + socket.inet_ntoa(ip_hdr[8]))
        print('dst ip:'+ socket.inet_ntoa(ip_hdr[9]))
        print('source port:',udp_hdr[0])
        print('destination port:', udp_hdr[1])
        print(data[0][42:])

s.close()