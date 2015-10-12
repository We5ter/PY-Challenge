#!/bin/bash
#coding=utf-8
import urllib,re
url="http://www.pythonchallenge.com/pc/def/ocr.html"
html=urllib.urlopen(url).read()
if not html:
    print "url error"
reg=re.compile("<!--(.*?)-->",re.S)
answer=re.findall(reg,html)
#print answer[1]
text=answer[1]
tmp=[]
for i in text:
#防止已计数字符重复计数
    if i in tmp:
        pass
    elif i=="\n":
        pass
    else:
        tmp.append(i)
        print i,text.count(i)
print tmp
