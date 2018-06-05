#!/usr/lib/python3.4
#-*-coding:utf-8-*-
import socket
import struct
import Ftp_module, ftp_send
sock_raw = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))#IP协议展开
url_dic = {'http://www.iqiyi.com/v_19rrdamyns.html': '[OPFansMaplesnow][One_Piece][806][MP4].mp4'}#重定向字典
test_dic = {'shoot' : '命中'}


while True:
    data = sock_raw.recvfrom(65535)
    print('开始接收')
    #print(type(data))
    #print(data)
    #dataunpack = struct.unpack(data)
    #print(dataunpack)
    ipHeader = data[0][0:20]
    tcpHeader = data[0][20:40]
    ip_hdr = struct.unpack("!BcHHHccH4s4s",ipHeader)#按格式展开IP头
    tcp_hdr = struct.unpack("!HHIIhhhh", tcpHeader)
    shift_ip = ip_hdr[0]
    shift_tcp = tcp_hdr[4]


    #print(ip_hdr)
    if '172.16' in socket.inet_ntoa(ip_hdr[8]):
        print('src:' + socket.inet_ntoa(ip_hdr[8]))
        print('dst:' + socket.inet_ntoa(ip_hdr[9]))
        if (b'http://www.iqiyi.com/v_19rrdamyns.html') in (data[0][20 + (((shift_tcp & 0xf000) >> 12) * 4):]):
            print(data[0][20 + (((shift_tcp & 0xf000) >> 12) * 4):])
            localpath = Ftp_module.downloadfile(url_dic['http://www.iqiyi.com/v_19rrdamyns.html'])
            UE_address = []  # 一个list,用于储存UE的IP地址与端口号
            UE_address.append('127.0.0.1')
            UE_address.append(12345)
            ftp_send.ftp_sendfile(tuple(UE_address), localpath)  # 发送FTP下载的文件
            break

