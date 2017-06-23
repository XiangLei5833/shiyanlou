#!/usr/bin/env python
from sys import getrefcount

a = [1,2,3]
print(getrefcount(a))    # reference count

b = a
print(getrefcount(b))
