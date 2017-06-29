#!/usr/bin/env python3
S = open('/home/shiyanlou/Code/String.txt')
s = S.read()
b = ''
for i in s:
    if i.isdigit():
        b = b+i
        
print(s)        
print(b)
