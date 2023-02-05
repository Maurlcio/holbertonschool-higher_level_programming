#!/usr/bin/python3
"""these are fun! i quite like these exercises. simple and to the point"""


class Rectangle:
    """rectangle class with, getter, setter, area and perimeter return,
    and it prints the rectangle with #s"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width + self.height) * 2)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        rectanglePrint = []
        for column in range(self.height):
            for row in range(self.width):
                rectanglePrint.append("#")
            if column != self.height - 1:
                rectanglePrint.append("\n")
        return ("".join(rectanglePrint))
