#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = count = 0
        list_length = sum(1 for _ in my_list)
        while (i < x):
            if (i == list_length or type(my_list[i]) == int):
                print("{:d}".format(my_list[i]), end='')
                count += 1
                i += 1
            else:
                i += 1
        print("")
        return count
    except IndexError:
        raise
