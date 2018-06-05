#!/usr/lib/python3.4
#-*-coding:utf-8-*-

from ftplib import FTP

def ftp_connect():
    ftp_host = '192.168.1.130'
    username = 'userftp'
    password = '123321123'
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(ftp_host, 21)
    ftp.login(username, password)
    return ftp

def downloadfile(remotefile):
    #remotepath = '/home/uftp/[OPFansMaplesnow][One_Piece][806][MP4].mp4'

    remotepath = '/home/uftp/' + remotefile
    localpath = '/home/nano/ftp测试/'+remotefile
    ftp = ftp_connect()#调用ftp初始化函数
    print(ftp.getwelcome())
    buffsize = 1024
    with open(localpath,'wb') as fp:
        ftp.retrbinary('RETR ' + remotepath,fp.write,buffsize)
        ftp.set_debuglevel(0)
    print('下载完成!\n')
    ftp.quit()
    return localpath



if __name__ == '__main__':
    remotefile = input("请输入想要下载的文件:")
    downloadfile(remotefile)
