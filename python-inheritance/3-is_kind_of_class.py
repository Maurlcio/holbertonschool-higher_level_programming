#!/usr/bin/python3
"""the shebang"""


def is_kind_of_class(obj, a_class):
    """checks if object is instance of class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
