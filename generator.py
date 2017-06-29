#!/usr/bin/env python3
def infinite_generator(start=0):
    while True:
        yield start
        start += 1    # 生成器是不可以重复使用的

for num in infinite_generator(4):
    print(num, end=' ')
    if num > 20:
        break
