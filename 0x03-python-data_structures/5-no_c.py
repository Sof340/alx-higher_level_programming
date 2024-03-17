#!/usr/bin/env python3


def no_c(my_string):
    new_list = []
    for c in my_string:
        if (c == "c" or c == "C"):
            continue
        else:
            new_list.append(c)
    new_string = ''.join(new_list)
    return new_string
