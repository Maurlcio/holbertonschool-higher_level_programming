#!/usr/bin/python3

for letter in range(ord("a"), ord("z")):
    txt = "{letter}"
    print(txt.format(letter = chr(letter)), end= '')
