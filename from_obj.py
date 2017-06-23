#!/usr/bin/env python
class from_obj(object):
    def __init__(self, to_obj):
        self.to_obj = to_obj


b = [1,2,3]
a = from_obj(b)
print(id(a.to_obj))
print(id(b))

# 容器对象包含的并不是元素对象本身，二十指向各个元素对象的引用
# 对象引用对象，是 Python 最基本的构成方式
