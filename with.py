#!/usr/bin/env python3

whth open('sample.txt') as fobj:    # 使用 with...as... 语句打开文件，会在文件用完后自行关闭。
    for line in fobj:
        print(line, end = '') 
