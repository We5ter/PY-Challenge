#!/bin/python
#coding=utf-8   
'''
图片模式： 
1 1位像素，黑和白，存成8位的像素 
L 8位像素，黑白 
P 8位像素，使用调色板映射到任何其他模式 
RGB 3×8位像素，真彩 
RGBA 4×8位像素，真彩+透明通道 
CMYK 4×8位像素，颜色隔离 
YCbCr 3×8位像素，彩色视频格式 
I 32位整型像素 
F 32位浮点型像素
'''
import urllib
from PIL import Image
   
file = open('oxygen.png', 'wb')
file.write(urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read())
file.close()
   
image = Image.open('oxygen.png')
data = image.convert('L').getdata()
   
message = []
for i in range(3,608,7):
        message.append(chr(data[image.size[0]*50+i]))
print ''.join(message)
print "-------------------------------"
print ''.join(map(chr,[105, 110, 116, 101, 103, 114, 105, 116, 121]))  
