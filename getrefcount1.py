#!/usr/bin/env python
from sys import getrefcount

a = [1,2,3]
b = a
print(getrefcount(b))

del a
print(getrefcount(b))
