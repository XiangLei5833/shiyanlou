#!/usr/bin/env
a = 1

def change_integer(a):
    a = a + 1
    return a

print change_integer(a)
print a    # 对于基础数据类型的变量，变量传递给函数之后，函数会在内存中复制一个新的变量，不影响原有变量


b = [1,2,3]

def change_list(b):
    b[0] = b[0] + 1
    return b

print change_list(b)
print b    # 对于表来说，表传递函数的是一个指针，指针指向序列中的位置，函数将会在表原有内存中进行操作。称为“指针传递”，一变皆变

