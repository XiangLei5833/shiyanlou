#!/usr/bin/env python
f = open('new.txt', 'w')
print(f.closed)
f.write('Hello World')
f.close()
print(f.closed)


