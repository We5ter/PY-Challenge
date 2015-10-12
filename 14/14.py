#!/bin/bash
#coding:utf-8
from PIL import Image

im=Image.open("wire.png")

print im.size
print im.mode

im14=Image.new(im.mode, (100,100))

directions=[(1,0),(0,1),(-1,0),(0,-1)]

def put(num,f):
    min,max=-1,num
    x=y=0
    direction=0
    for i in range(num*num):
        if (not min<x+directions[direction][0]<max) or (not min<y+directions[direction][1]<max) or(x==min+1 and y==min+2):
            direction+=1
            if direction is 4:
                direction=0
                min+=1
                max-=1
        apply(f,((x,y),))
        x+=directions[direction][0]
        y+=directions[direction][1]
        
    
res=[]
put(100,res.append)
for i,item in enumerate(res):
    im14.putpixel(item,im.getpixel((i,0)))
im14.save('answer.jpg')
