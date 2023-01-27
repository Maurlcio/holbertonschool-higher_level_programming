#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    for i in set_1:
        if i not in set_2:
            new_list.append(i)
    for x in set_2:
        if x not in set_1:
            new_list.append(x)
    return new_list
