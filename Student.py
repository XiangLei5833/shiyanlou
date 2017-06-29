#!/usr/bin/env python3

class Student(object):
    def __init__(self, name):
        self.name = name

    def student_details(self):
        return self.name


std = Student("Kushal")
print(std.name)
std.name = "Python"    # 第二次直接调用属性即可，因为 std 已经被类赋值
print(std.name)
