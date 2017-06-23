#!/usr/bin/env python
class Bird(object):
   feather = True


class Chicken(Bird):
    fly = False
   
    def __init__(self,age):
        self.age = age

summer = Chicken(2)
print(Bird.__dict__)
print(Chicken.__dict__)
print(summer.__dict__)

summer.__class__    # __class__ 属性查找对象 summer 的类
summer.__base__     # __base__ 属性用来查询 summer 的父类


