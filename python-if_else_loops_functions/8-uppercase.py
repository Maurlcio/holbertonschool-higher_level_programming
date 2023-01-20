#!/usr/bin/python3
def uppercase(string):
    for i in string:
        if ord(i) in range(97, 123):
            print("{}".format(chr(ord(i) - 32)), end='')
        else:
            print("{}".format(i), end='')
    print(f"")
