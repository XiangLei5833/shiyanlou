import os

def view_dir(path = '.'):
    """这个函数打印给定目录中所有文件和目录
     :args path: 指定目录，模认为当前目录
     """
    names = os.listdir(path)
    names.sort()
    for name in names:
        print(name, end = ' ')
    print()


view_dir('/')
