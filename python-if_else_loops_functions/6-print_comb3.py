#!/usr/bin/python3

for y in range(0, 9):
    z = y + 1
    for x in range(z, 10):
        if y in [8] and x in [9]:
            print("89")
        else:
            print("{}{}, ".format(y, x), end='')
