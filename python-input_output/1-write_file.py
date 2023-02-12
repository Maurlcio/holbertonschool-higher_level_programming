#!/usr/bin/python3
"""the shebang"""


def write_file(filename="", text=""):
    """Writes a string of text to a UTF8 text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
