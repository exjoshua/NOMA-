#!/usr/lib/python3.4

import os
from urllib import request

url = "https://blog.csdn.net/u014804795/article/details/52227518" #网页地址
wp = request.urlopen(url)
content = wp.read()
with open('/home/nano/test.html', 'w+b') as f:
    f.write(content)



os.system('firefox /home/nano/test.html')