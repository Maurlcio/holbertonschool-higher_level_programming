#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 1:
        b = tuple_a[1]
    else:
        b = 0

    if len(tuple_a) > 0:
        a = tuple_a[0]
    else:
        a = 0

    if len(tuple_b) > 1:
        y = tuple_b[1]
    else:
        y = 0

    if len(tuple_b) > 0:
        x = tuple_b[0]
    else:
        x = 0

    new_one = a + x
    new_two = b + y

    new_tuple = (new_one, new_two)
    return new_tuple
