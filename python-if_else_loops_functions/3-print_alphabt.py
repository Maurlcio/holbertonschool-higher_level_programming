#!/usr/bin/python3

for letter in range(ord("a"), (ord("z") + 1)):
    if letter in [101, 113]:
        continue
    txt = "{letter}"
    print(txt.format(letter=chr(letter)), end='')
