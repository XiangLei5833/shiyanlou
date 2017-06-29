class Complex:
    def __init__(self, realpart, imagpart):    # 参数通过 __init__() 传递到类的实例化操作上，类的实例化操作会自动为新创建的类实例调用 __init__() 方法
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)    # 进行类的实例化操作
print(x.r,x.i)
