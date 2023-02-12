#!/usr/bin/python3
"""the shebang"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        print(sorted(self))
