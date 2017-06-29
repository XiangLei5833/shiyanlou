#!/usr/bin/env python3
a = ['Pradeepto','Kushal']
b = ['OpenSUSE', 'Fedora']
for x,y in zip(a,b):
    print("{} uses {}".format(x,y))

# 上面运用zip()函数遍历两个序列类型，合而为一
