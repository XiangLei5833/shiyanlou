#!/usr/bin/env python
# -*- coding: utf-8 -*-

class OldCourse(object):
    """ 老的课程类 """
    def show(self):
        """ 显示关于本课程的所有信息 """
        print("show description")
        print("show teacher of course")
        print("show labs")


class Page(object):
    """ 使用本课程的客户端 """
    def __init__(self, course):
        self.course = course

    def render(self):
        self.course.show()


class NewCourse(object):
    """ 新的课程类，为了模块化显示课程信息，实现了新的课程类 """
    def show_desc(self):
        """ 显示描述信息 """
        print("show description")

    def show_teacher(self):
        """ 显示老师信息 """
        print("show teacher of course")

    def show_labs(self):
        """ 显示实验 """
        print("show labs")


class Adapter(object):
    """
     适配器，尽管实现了新的课程类，但是很多代码中还是需要使用 Oldcourse.show()       方法
     """

    def __init__(self, course):
        self.course = course

    def show(self):
        """ 适配方法，调用真正的操作 """
        self.course.show_desc()
        self.course.show_teacher()
        self.course.show_labs()

if __name__ == '__main__':
    old_course = OldCourse()
    page = Page(old_course)
    page.render()
    print("")
    new_course = NewCourse()
    # 新课程类没有 show 方法，需要使用适配器进行适配。
    adapter = Adapter(new_course)
    page = Page(adapter)
    page.render()

# 适配器模式就是将一个类的接口变换成客户端所期待的另一种接口，使原本不兼容的两个类能够一起工作，适配器就相当于一个格式转换器
