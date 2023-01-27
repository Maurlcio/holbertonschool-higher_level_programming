#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for i in set_1:
        if i not in set_2:
            new_list.append(i)
    for l in set_2:
        if l not in set_1:
            new_list.append(l)
    return new_list

