#!/usr/bin/python3
"""the shebang"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""yup, there it is, its see who it is"""


class Rectangle(BaseGeometry):
    """inheritance class"""
    def __init__(self, width, height):
        """yup, there it is"""
        super().integer_validator("width", width)
        self.__width = width
        super()integer_validator("height", height)
        self.__height = height

    def area(self):
        """its look who it is"""
        return self.__width * self.__height

    def __str__(self):
        """as in, look who it is"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
