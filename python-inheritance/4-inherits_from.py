#!/usr/bin/python3
"""the shebang"""


def inherits_from(obj, a_class):
    """checks if object is inherited from a class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
