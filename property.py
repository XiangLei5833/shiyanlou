#!/usr/bin/env python

class Bird(object):
    feather = True


class Chicken(Bird):
    fly = False
     
    def __init__(self, age):
        self.age = age
   
    def getAdult(self):
        if self.age > 1: return True
        else: return False
    adult = property(getAdult)


summer = Chicken(2)
print(summer.adult)
summer.age = 0.5
print(summer.adult)
