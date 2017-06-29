#!/usr/bin/env python3
import sys

def Hours():
    try:
        a = int(sys.argv[1])
        if a > 0:
            print("{} H, {} M".format(*divmod(a,60)))        
        else:
            raise ValueError()
    except ValueError:
         print("ValueError: Input number cannot be negative")

if __name__ == '__main__':
     if len(sys.argv[1]) > 0:
         Hours()
     else:
         sys.exit[1]
        
