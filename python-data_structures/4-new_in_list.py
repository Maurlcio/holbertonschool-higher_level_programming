#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = []
    if idx < 0 or idx > (len(my_list) - 1):
        copy = my_list
        return copy
    else:
        copy = my_list.copy()
        copy[idx] = element
        return copy
