#UE侧接收字节流程序
#!/usr/lib/python3.4
#-*-coding:utf-8-*-


import socket
import threading,os,struct

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
local_address = ('127.0.0.1', 12345)
s.bind(local_address)
s.listen(5)


def read_filebyte(sock,addr):
    print('收到新的连接:%s:%s' %addr)
    while True:
        file_infosize = struct.calcsize('128sl')
        buf = sock.recv(file_infosize)
        if buf:
            filename, filesize = struct.unpack('128sl', buf)
            print('filesize is:', filesize)
            filenewname = os.path.join('/home/nano/',('new_' + filename.decode('utf-8')).strip('\00'))
            print('newfile name is:\n',os.path.basename(filenewname))
            recvd_size = 0
            with open(filenewname,'wb') as file:
                while not recvd_size == filesize:
                    if filesize - recvd_size > 1024:
                        rdata = sock.recv(1024)
                        recvd_size += len(rdata)
                    else:
                        rdata = sock.recv(filesize - recvd_size)
                        recvd_size = filesize
                    file.write(rdata)

            print('receive done')


while True:
    sock, addr = s.accept()
    print('等待新的连接.....')
    t = threading.Thread(target=read_filebyte,args=(sock, addr))
    t.start()
s.close()