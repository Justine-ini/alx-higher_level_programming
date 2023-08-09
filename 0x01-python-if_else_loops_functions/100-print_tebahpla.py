#!/usr/bin/python3
for i in range(26):
    if i % 2 == 0:
        print("{}".format(chr(ord('z') - i)))
    else:
        print("{}".format(chr(ord('Z') - i)))
