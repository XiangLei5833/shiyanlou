#!/usr/bin/env python3
S = open('/home/shiyanlou/Code/String.txt')
s = S.read()
a = []
for i in s:
    if i.isdigit():
        a.append(i)
b = "".join(a)
print(b)
