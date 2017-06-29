#!/usr/bin/env python3
# 此方法可以用于之前那个求解二次方程式；用于多次循环，直到有解
while True:
    n = int(input("Please enter an Integer: "))
    if n < 0:
        continue
    elif n == 0:
        break
    print("Square is", n ** 2)
print("Goodbye")
