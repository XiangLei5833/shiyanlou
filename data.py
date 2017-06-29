#!/usr/bin/env python3
data = {'Kushal': 'Fedora', 'Jack':'Mac'}
for x, y in data.items():
    print("{} uses {}".format(x,y))

运用items()函数将data字典化为以字典每个键值为单个元素的元组。
