#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Lamp(object):
    def power_off(self):
        print("Lamp power off")


class Fan(object):
    def switch_off(self):
        print("Fan switch off")


class Tv(object):
    def off(self):
        print("Tv off")


class Person(object):
    def __init__(self):
        self.lamp = Lamp()
        self.fan = Fan()
        self.tv = Tv()

    def leave_home(self):
        self.lamp.power_off()
        self.fan.switch_off()
        self.tv.off()


class Facade(object):
    def __init__(self):
        self.lamp = Lamp()
        self.fan = Fan()
        self.tv = Tv()

    def can_be_leave(self):
        if self.lamp.power_off() and self.fan.switch_off() and self.tv.off():
            return True
        else:
            return False


class New_Person(object):
    def __init__(self, facade):
        self.facade = facade

    def leave_home(self):
        if self.facade.can_be_leave:
            print("all off")
        else:
            print("no")



if __name__ == '__main__':
    Person.leave_home()
    
    print("Use Facade")
    facade = Facade(self)
    facade_person = New_Person(facade)
    facade_person.leave.home()
     
