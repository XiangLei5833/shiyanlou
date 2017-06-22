#!/usr/bin/env python
# -*- coding: utf-8 -*-

class User(object):
    """ 用户类 """
    def is_login(self):
        return True

    def has_privilege(self, privilege):
        return True


class Course(object):
    """ 课程类 """
    def can_be_learned(self):
        return True


class Lab(object):
    """ 实验类 """
    def can_be_started(self):
        return True


class Client(object):
    """ 客户类，用于开始一个实验 """
    def __init__(self, user, course, lab):
        self.user = user
        self.course = course
        self.lab = lab

    def start_lab(self):
        """
         开始实验，需要经过一系列的判断：用户是否登录，课程是否可以学习，实验是          否可以开始。
         
         """
        if self.user.is_login() and self.course.can_be_learned() and self.lab.can_be_started():
            print("start lab")
        else:
            print("can not start lab")


class FacadeLab(object):
    """ 新的 Lab 类，应用了面向对象模式 """
    def __init__(self, user, course, lab):
        self.user = user
        self.course = course
        self.lab = lab

    def can_be_started(self):
        if self.user.is_login() and self.course.can_be_learned() and self.lab.can_be_started():
            return True
        else:
            return False


class NewClient(object):
    """ 新的客户类，使用外观模式 """
    def __init__(self, facade_lab):
        self.lab = facade_lab

    def start_lab(self):
        """ 开始实验，只需要判断 FacadeLab 是否可以开始 """
        if self.lab.can_be_started:
            print("start lab")
        else:
            print("can not start lab")


if __name__ == '__main__':
    user = User()
    course = Course()
    lab = Lab()
    client = Client(user, course, lab)
    client.start_lab()

    print("User Facade Pattern")
    facade_lab = FacadeLab(user, course, lab)
    facade_client = NewClient(facade_lab)
    facade_client.start_lab()
       
# 外观模式主要目的在于降低系统的复杂程度，在面相对想软件系统中，类和类之间的关系越多，不能表示系统设计的越好，反而表示系统中类之间的耦合度太大，维护和修改都缺乏灵活性。 
