#!/usr/bin/env python
import signal

def myHandler(signum, frame):
    print('I received', signum)

signal.signal(signal.SIGTSTP, myHandler)
signal.pause()
print('End of Signal Demo')
