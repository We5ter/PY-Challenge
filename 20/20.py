#!/bin/bash/python
#coding=utf-8

import urllib,re  
url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'  
#start = 30203  
#start = 2123456743  
start = 1152983631  
end = 2123456789  
find = re.compile(r'bytes \d*-(\d*)')  
while start<end:  
    opener = urllib.FancyURLopener()  
    opener.addheader('Range','bytes=%d-%d' % (start,end))  
    f = opener.open(url)  
    start = re.findall(find,str(f.info()))  
    if len(start)>0:  
        start = int(start[0])+1  
    print f.info()      
    open(r'out.zip','wb').write(f.read());break  
