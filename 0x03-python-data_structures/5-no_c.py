#!/usr/bin/env python3


def no_c(my_string):
    str_list = list(my_string)
    a = str_list.count("c")
    b = str_list.count("C")
    while (a > 0):
        str_list.remove("c")
        a -= 1
    while (b > 0):
        str_list.remove("C")
        b -= 1
    my_string = ''.join(str_list)
    return my_string
