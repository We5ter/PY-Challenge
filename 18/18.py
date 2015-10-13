#!/bin/bash/python
#coding=utf-8
'''
from PIL import Image
#first try start
im=Image.open('balloons.jpg','wb')
w,h=im.size
diff=Image.new(im.mode,(w/2,h),0)
for i in range(w/2):
    for j in range(h):
        diff.putpixel((i,j),tuple([x[0]-x[1] for x in zip(im.getpixel((i,j)),im.getpixel((i+w//2,j)))]))
        diff.save('diff.png')
#first try end
'''

import gzip,difflib,urllib2
    
h = gzip.open("deltas.gz")    
   
part_1, part_2 = [], []  
pic_1,pic_2, pic_3 = [], [], []  
   
for line in h:  
    part_1.append(line[0:53])  
    part_2.append(line[56:-1])  
   
h.close()  
   
for line in list(difflib.Differ().compare(part_1, part_2)):  
    if line[0] == "+":  
        pic_1.append(line[2:])  
    elif line[0] == "-":  
        pic_2.append(line[2:])  
    else:  
        pic_3.append(line[2:])  
   
for n, data in enumerate((pic_1, pic_2, pic_3)):  
    temp = []  
   
    for line in data:  
        temp.extend([chr(int(o, 16)) for o in line.strip().split(" ") if o])  
   
    h = open("%s.png" % (n + 1), "wb")  
    h.writelines(temp)  
    h.close()  
