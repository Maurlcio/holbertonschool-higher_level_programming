#!/usr/bin/python3
"""its still a square i really dont know what youre expecting form me here"""


class Square:
    """initiates private attribute size assuming it fulfils
    certain conditions. also, retrieves the area of a square,
    also, does getter and setter patern. also also, prints the square
    with #s. also, handles position.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(self.__position[0])) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(self.__position[1])) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (self.__position[0] < 0 or self.__position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for space2 in range(self.__position[1]):
                print()
            for column in range(self.__size):
                for space1 in range(self.__position[0]):
                    print(" ", end='')
                for row in range(self.__size):
                    print("#", end='')
                if (column + 1) < self.__size:
                    print()
            print()
