def high(func, value):
    return func(value)

lst = high(dir, int)
print(lst[-3:])

# 此为高阶函数:
# 使用一个或者多个函数作参数；
# 返回另一个函数作为输出。

