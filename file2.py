#!/usr/bin/env python
with open('new.txt', 'w') as f:    # context manager
    print(f.closed)
    f.write("Hello World!")
print(f.closed)


