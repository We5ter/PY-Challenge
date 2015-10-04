#!/bin/bash
#coding=utf-8
#next:linkedlist.html->linkedlist.php
import urllib,re
url="http://www.pythonchallenge.com/pc/def/equality.html"
html=urllib.urlopen(url).read()
if not html:
    print "url error"
reg=re.compile("<!-(.*?)-->",re.S)
answer=re.findall(reg,html)
str=answer[0]
patt=re.findall("[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}",str)
#print patt
for i in patt:
    print i[4]
