#!/usr/bin/env python3
def add_number(num):
    def adder(number):    # adder()就是一个闭包，闭包是由一个函数返回的函数
        return num + number
    return adder

a_10 = add_number(10)
print(a_10(21))
