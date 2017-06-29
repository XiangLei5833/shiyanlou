#!/usr/bin/env python3
import sys
from collections import Counter


class Person(object):
    def __init__(self, score):
        self.score = score

    def get_grade(self):
        self.score = sys.argv[2]
        return self.score


class Student(Person):
    def __init__(self, score):
        Person.__init__(self, score)

    def get_grade(self):
        """
        返回包含学生具体信息的字符串
        """
        pass_count = 0
        fail_count = 0
        for i in list(self.score):
            if i != 'D':
                pass_count += 1
            else:
                fail_count += 1
        return "pass:{}, fail:{}".format(pass_count, fail_count)
        
class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, score):
        Person.__init__(self, score)
      
    def get_grade(self):
        return "{}:{}".format(*Counter(self.score))


if __name__ == '__main__':
    if sys.argv[1] == 'student':
        print(Student.get_grade(self))
    elif sys.argv[1] == 'teacher':
        print(Teacher.get_grade(self))
        
