#!/usr/bin/python3
"""its still a square i really dont know what youre expecting form me here"""


class Square:
    """initiates private attribute size assuming it fulfils
    certain conditions. also, retrieves the area of a square,
    also, does getter and setter patern. also also, prints the square
    with #s.
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size > 0:
            for column in range(self.__size):
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
