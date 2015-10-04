#!/bin/bash
#coding=utf-8
import re,urllib,sys

#每次中断请修改nothing，然后keep going~（12345->16044->8022->82683->82682->63579)
nothing="8022"
base_url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
url=base_url+nothing
#print html
count=1
while nothing:
    try:
        html=urllib.urlopen(url).read()
        patt=re.findall("[0-9]+",html)
        nothing=patt[0]
        print count,"\n",url
        url=base_url+nothing
        count+=1
    except:
        print "the last url is:\n"
        print url,'\n',html
        sys.exit(-1)
