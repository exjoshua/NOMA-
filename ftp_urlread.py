#eNB or EPC判断文件是否存在于边缘服务器
#!/usr/lib/python3.4
#-*-coding:utf-8-*-

import Ftp_module, ftp_send
import socket
import struct

sock_raw = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0003))
url_dic = {'http://www.iqiyi.com/v_19rrdamyns.html': '[OPFansMaplesnow][One_Piece][806][MP4].mp4'}#重定向字典
test_dic = {'shoot' : '命中'}
while True:
    data = sock_raw.recvfrom(65535)
    ethheader = data[0][14]
    ipHeader = data[0][14:34]
    tcpHeader = data[0][34:54]

    ip_hdr = struct.unpack("!BcHHHccH4s4s",ipHeader)#按格式展开IP头
    print('src:' + socket.inet_ntoa(ip_hdr[8]))
    print('dst:' + socket.inet_ntoa(ip_hdr[9]))
    if ip_hdr[6] == b'\x06':        #如果是IP协议
        if len(data[0]) >= 54:      #如果是TCP协议且有内容
            tcp_hdr = struct.unpack("!HHIIhhhh",tcpHeader)#源端口、目的地端口、序号、确认序号、（首部长度+保留+标志位）、校验和、紧急指针、选项
            #print(ip_hdr)
            shift_ip = ip_hdr[0]
            #print('ip首部长度为:', (shift_ip & 0x0f) * 4)
            #print(tcp_hdr)
            shift_tcp = tcp_hdr[4]
            #print('tcp首部长度为:', ((shift_tcp & 0xf000) >> 12) * 4)
            #print('src:' + socket.inet_ntoa(ip_hdr[8]))
            #print('dst:'+ socket.inet_ntoa(ip_hdr[9]))
            #print('src port:', tcp_hdr[1])
            #print('dst port:', tcp_hdr[0])
            if socket.inet_ntoa(ip_hdr[9]) == '192.168.1.222': #如果是本机发送的请求
                if (b'http://www.iqiyi.com/v_19rrdamyns.html') in (data[0][34+(((shift_tcp & 0xf000) >> 12) * 4):]):
                    print(test_dic['shoot'])
                    print(data[0][34+(((shift_tcp & 0xf000) >> 12) * 4):])
                    localpath = Ftp_module.downloadfile(url_dic['http://www.iqiyi.com/v_19rrdamyns.html'])
                    UE_address = []#一个list,用于储存UE的IP地址与端口号
                    UE_address.append('127.0.0.1')
                    UE_address.append(12345)
                    ftp_send.ftp_sendfile(tuple(UE_address), localpath)#发送FTP下载的文件
                    break
                    #Ftp_module.downloadfile(url_dic['http://www.iqiyi.com/v_19rrdamyns.html'])

sock_raw.close()
print('跳出循环!')


#Ftp_module.downloadfile(url_dic['http://www.iqiyi.com/v_19rrdamyns.html'])