#!/usr/bin/python3
"""its still a square i really dont know what youre expecting form me here"""


class Square:
    """initiates private attribute size assuming it fulfils
    certain conditions. also, retrieves the area of a square
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
