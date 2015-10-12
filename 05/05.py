#！/bin/bash
#coding=utf-8

import urllib,pickle
url="http://www.pythonchallenge.com/pc/def/banner.p"
html=urllib.urlopen(url).read()
list = pickle.loads(html)  
#print list
output = open('output.txt', 'w')    
for line in list:    
    print >> output, ''.join([c[0]*c[1] for c in line])  
output.close() 
#output.txt为channel字样
