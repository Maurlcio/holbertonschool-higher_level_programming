#!/usr/bin/python3
"""the shebang"""


def is_same_class(obj, a_class):
    """Checks if an object is EXACTLY an instance of a class"""
    if type(obj) == a_class:
        return True
    else:
        return False
