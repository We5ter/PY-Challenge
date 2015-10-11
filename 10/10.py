#!/bin/bash
#coding:UTF-8
import re

if __name__ == '__main__':
    
    counter = 0
    
    def fun(s):
        
        result = ''
        
        char = s[0]
        count = 0
                    
        for x in s:
            if x == char:
                count += 1
            else:
                result += str(count) + char
                count = 1
                char = x
                
        result += str(count) + char
        
        #print(result)
        
        global counter
        counter += 1
        
        if counter <= 30:
            fun(result)
            result1=str(result)
            print "----------------------------------"
            print len(result1)    
    fun('1')

