#!/usr/bin/env python
import subprocess
child = subprocess.Popen(["ping","-c","5","www.baidu.com"])
print("parent process")
