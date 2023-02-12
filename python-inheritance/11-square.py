#!/usr/bin/python3
"""the shebang"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """all comes together"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
