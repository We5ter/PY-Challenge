#!/bin/bash
#coding:utf-8
import base64

text=open('attachment.txt','r').read()
music=open('indian.wav','wb')
wav=base64.b64decode(text)
music.write(wav)
music.close()
#看了le4f的解答
import wave
wi = wave.open('indian.wav','rb')
wo = wave.open('indian_out.wav','wb')
#将第一段声音的全部信息同样写入第二段
wo.setparams(wi.getparams())
#获取声音的帧的数量
for i in range(wi.getnframes()):
#从最后一个帧开始每次读入一个帧并写入新的wav
    wo.writeframes(wi.readframes(1)[::-1])  
wi.close()
wo.close()
