#!/usr/bin/env python3
lst = [1,2,3,4,5]
def square(num):
    return num * num

print(list(map(square, lst)))    # map() 是高阶函数，参数分别为一个函数和一个序列（迭代器），对序列每个值应用该函数，并返回一个新的序列（迭代器）。
