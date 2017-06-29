#!/usr/bin/env python3
class Counter(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        counter = self.low
        while self.high >= counter:
            yield counter
            counter += 1

gobj = Counter(5,10)
for num in gobj:
    print(num, end=' ')

# 创建可重复使用生成器的方式是不保存任何状态的基于对象的生成器。
