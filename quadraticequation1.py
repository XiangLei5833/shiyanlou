#!/usr/bin/env python3
import math
while True:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))
    d = b*b - 4*a*c
    if d < 0:
        print("ROOT is imaginary")
        continue
    else:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        print('root1 = ', root1)
        print('root2 = ', root2)
        break
       

