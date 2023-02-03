#!/usr/bin/python3
"""I like this exercise! Making the square is a fun bit of visual math"""


def print_square(size):
    """Prints out a square of variable size as long as it's given
    a valid size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
