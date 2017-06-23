#!/usr/bin/env python

year = int(input("Enter a year: "))

if year % 100 == 0:
    if year % 4 == 0:
        print 'True'
    else:
        print 'False'
elif year % 4 == 0:
    print 'True'
else:
    print 'False'
