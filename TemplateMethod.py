#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc


class Fishing(object):
    """ 钓鱼模板基类 """
    __metaclass__ = abc.ABCMeta
    
    def finishing(self):
        """ 钓鱼方法中，确定了要执行哪些操作才能钓鱼 """
        self.prepare_bait()
        self.go_to_riverbank()
        self.find_location()
        print("start fishing")

    @abc.abstractmethod
    def prepare_bait(self):
        pass

    @abc.abstractmethod
    def go_to_riverbank(self):
        pass

    @abc.abstractmethod
    def find_location(self):
        pass


class JohnFishing(Fishing):
    """ John 去钓鱼，先实现三步骤 """
    def prepare_bait(self):
        """ 具体步骤 """
        print("John: buy bait from Taobao")
    
    def go_to_riverbank(self):
        print("John: to river by driving")

    def find_location(self):
        print("John: select location on the island")



class SimonFishing(Fishing):
    """ Simon 也去钓鱼，同样实现三步骤 """
    def propare_bait(self):
        print("Simon: buy bait from JD")

    def go_to_riverbank(self):
        print("Simon: to river by biking")

    def find_location(self):
        print("Simon: select location on the riverbank")


if __name__ == '__main__':
    f = JohnFishing()
    f.finishing()

    f = SimonFinshing()
    f.finishing()
