#!/usr/bin/env python
def line_conf():
    b = 15
    def line(x):
        return x*2+b
    return line


b = 5
my_line = line_conf()
print(my_line.__closure__)
print(my_line.__closure__[0].cell_contents)    # 环境变量的取值被报存在函数对象的 __closure__ 属性中， __closure__中包含一个元组，元组中每个元素都是 cell 类型的对象
