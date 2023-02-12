#!/usr/bin/python3
"""the shebang"""


def read_file(filename=""):
    """Prints the contents of a text file"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
