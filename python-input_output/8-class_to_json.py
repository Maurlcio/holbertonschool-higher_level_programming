#!/usr/bin/python3
"""the shebang"""


def class_to_json(obj):
    """returns dict for json"""
    return obj.__dict__
