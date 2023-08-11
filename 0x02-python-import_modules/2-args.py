#!/usr/bin/python3
import sys
num = len(sys.argv)
print("{} arguments:".format(num - 1))
for i in range(1, num):
    print("{}: {}".format(i, sys.argv[i]))
