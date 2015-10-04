#!/bin/bash
#coding=utf-8
#下载http://www.pythonchallenge.com/pc/def/channel.zip
#输出hockey,访问hockey.html提示it's in the air,那就是oxygen.html 
import re,zipfile
   
number = "90052"
zip_file = zipfile.ZipFile("channel.zip", "r")
   
comments = []
for i in range(1000):
        comments.append(zip_file.getinfo("%s.txt" % number).comment)
        numbers = re.findall('([0-9]+)$', zip_file.read("%s.txt" % number))
        try:
                number = numbers[0]
        except:
                print ''.join(comments)
                break
