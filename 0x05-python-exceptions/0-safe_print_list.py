#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        count = 0
        while (i < x):
            print("{:d}".format(my_list[i]), end='')
            count += 1
            i += 1
        print("")
        return count
    except IndexError:
        print("")
        return count