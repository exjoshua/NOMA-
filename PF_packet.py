#!/usr/lib/python3.4
import socket
import struct
import binascii
sock_raw = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0003))
while True:
    data = sock_raw.recvfrom(65535)
    ethheader = data[0][14]
    ipHeader = data[0][14:34]
    tcpHeader = data[0][34:54]

    ip_hdr = struct.unpack("!BcHHHccH4s4s",ipHeader)#按格式展开IP头

    #tmp_data = binascii.a2b_hex(data[0][0:40])
    #print(tmp_data)
    #print('tcp header:',tcp_hdr)
    #print('src port :', tcp_hdr[1])
    #print('dst port :' , tcp_hdr[0])
    #if socket.inet_ntoa(ip_hdr[1]) == '61.135.169.125':
        #print('recv iqiyi!')

    if ip_hdr[6] == b'\x06':        #如果是IP协议
        if len(data[0]) >= 54:      #如果是TCP协议且有内容
            tcp_hdr = struct.unpack("!HHIIhhhh",tcpHeader)#源端口、目的地端口、序号、确认序号、（首部长度+保留+标志位）、校验和、紧急指针、选项
            print(ip_hdr)
            shift_ip = ip_hdr[0]
            print('ip首部长度为:', (shift_ip & 0x0f) * 4)
            print(tcp_hdr)
            shift_tcp = tcp_hdr[4]
            print('tcp首部长度为:', ((shift_tcp & 0xf000) >> 12) * 4)
            #print('src:' + socket.inet_ntoa(ip_hdr[8]))
            #print('dst:'+ socket.inet_ntoa(ip_hdr[9]))
            #print('src port:', tcp_hdr[1])
            #print('dst port:', tcp_hdr[0])
            if socket.inet_ntoa(ip_hdr[8]) == '192.168.1.222':
                if len(data[0])>100:
                    with open('/home/nano/Http_content.txt','wb+') as fff:
                            fff.write(data[0][54:])
                            print('发送请求:')
                            print(data[0][34+(((shift_tcp & 0xf000) >> 12) * 4):])

                            #print(data[0][54:].decode("UTF-8"))


            elif socket.inet_ntoa(ip_hdr[9]) == '192.168.1.222' :
                print("接受请求：")
                print(data[0][34+(((shift_tcp & 0xf000) >> 12) * 4):])


