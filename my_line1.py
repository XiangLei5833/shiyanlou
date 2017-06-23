#!/sur/bin/env python
def line_conf():
    b = 15    # enbironment virable, b 是 line 的俄环境变量，虽然 b 的信息存在line 的定义之外。
    def line(x):    # line 参照的 b 值是函数定义时可供参考的b 值，而不是使用时的 b 值。
        return 2*x+b
    return line


b = 5
my_line = line_conf()
print(my_line(5))

# 一个函数和他的环境变量结合在一起，就构成了一个闭包。即为一个包含有环境变量取值的函数对象。
