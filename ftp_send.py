#将接收到的FTP字节流直接发送给UE侧
#!/usr/lib/python3.4
#-*-coding:utf-8-*-

import socket
import os, struct


def ftp_sendfile(addr,localpath = '/home/nano/openair-cn'):
    ftp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ftp_sock.connect(addr)
    print('连接上了!')
    while True:
        #file_path = input('Please Enter File Path:\r\n')
        if os.path.isfile(localpath): #如果文件存在
            print('进入')
            fileinfo_size = struct.calcsize('128sl')#定义打包规则
            #定义文件头信息,包含文件名和大小
            byte_filepath = bytes(os.path.basename(localpath),encoding='utf-8')
            fhead = struct.pack('128sl', byte_filepath, os.stat(localpath).st_size)
            ftp_sock.send(fhead)
            fo = open(localpath, 'rb')
            while True:
                filedata = fo.read(1024)
                if not filedata:
                    break
                ftp_sock.send(filedata)
            fo.close()
            print('send over...')
            break
    ftp_sock.close()

if __name__ == '__main__':
    ftp_sendfile(('127.0.0.1',12345))

