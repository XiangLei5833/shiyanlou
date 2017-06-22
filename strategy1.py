#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc


class AbsShow(object):
    """ 抽象显示对象 """
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def show(self):
        pass


class AdminShow(AbsShow):
    """ 管理员的显示操作 """
    def show(self):
        return "show with admin"


class UserShow(AbsShow):
    """ 普通用户的显示操作 """
    def show(self):
        return "show with user"


class Question(object):
    """ 问题对象，使用策略模式之后的做法 """
    def __init__(self, show_obj):
        self.show_obj = show_obj
    
    def show(self):
        return self.show_obj.show()


if __name__ == '__main__':
    q = Question(show_obj=AdminShow())
    print(q.show())
    # 替换原来的显示对象， 体现策略模式的互换行为
    q.show_obj = UserShow()
    print(q.show())

# 策略模式就是将各种操作（算法）进行封装，并使他们之间可以互换
