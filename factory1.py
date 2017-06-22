#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class BasicCourse(object):
    def get_labs(self):
        return "basic_course: labs"

    def __str__(self):
        return "BasciCourse"


class ProjectCourse(object):
    def get_labs(self):
        return "project_course: labs"
    
    def __str__(self):
        return "ProjectCourse"


class SimpleCourseFactory(object):
    @staticmethod
    def create_course(type):
        if type == 'bc':
            return BasicCourse()
        elif type == 'pc':
            return ProjectCourse()


if __name__ == '__main__':
    t = random.choice(['bc','pc'])
    course = SimpleCourseFactory.create_course(t)
    print (course.get_labs)
