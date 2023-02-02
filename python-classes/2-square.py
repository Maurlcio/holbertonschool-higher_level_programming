#!/usr/bin/python3
"""defines a class called square with certain attributes"""


class Square:
    """initiates private attribute size assuming it fulfils
    certain conditions
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
