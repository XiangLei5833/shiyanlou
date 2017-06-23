#!/usr/bin/env python
def line_conf(a, b):    # 函数 line 和环境变量 a,b 构成闭包
    def line(x):
        return a*x+b
    return line


line1 = line_conf(1,1)
line2 = line_conf(4,5)
print(line1(5), line2(5))    # 里面的 5 指的是 x
