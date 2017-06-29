#!/usr/bin/env python3

name = input("Enter the fiel name: ")
fobj = open(name)
print(fobj.read())    # 第二次调用 read() 返回空字符串，因为它已经读取了完整的字符串。
fobj.close()    # 打开文件后总是要关闭文件，因为程序所能打开的文件数量是有限的，且每个打开的文件都会占用内存资源。
               

