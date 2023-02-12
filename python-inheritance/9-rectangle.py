#!/usr/bin/python3
"""Represents a rectangle using a prior thing"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super()integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns print() and str() correctly"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
