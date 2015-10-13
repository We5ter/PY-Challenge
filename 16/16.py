#!/bin/bash
#coding:utf-8

from PIL import Image

im=Image.open("mozart.gif")

#print im.size

#print im.mode

print im.getpixel((630,2))

def straighten(line): 
    i=0
    while line[i]!=195:
        i+=1
    return line[i:]+line[:i]

for h in range(im.size[1]):
    line=[im.getpixel((w,h)) for w in range(im.size[0])]
    line=straighten(line)
    [im.putpixel((w,h),line[w]) for w in range(im.size[0])]

im.save('answer.gif')

print "done"
