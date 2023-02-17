#!/usr/bin/python3
"""the shebang"""


class Base:
    """class that will serve as a base for all the other ones"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
