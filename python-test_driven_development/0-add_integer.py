#!/usr/bin/python3
"""Adds up two integers while repurposing floats to ints"""


def add_integer(a, b=98):
    """Adds up two ints and returns the sum. Accepts floats,
    but they get typecasted to ints first
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
