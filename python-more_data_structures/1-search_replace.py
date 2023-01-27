#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    i = new_list.count(search)

    while i > 0:
        idx = new_list.index(search)
        new_list.pop(idx)
        new_list.insert(idx, replace)
        i -= 1
    return new_list
