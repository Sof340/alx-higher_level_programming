#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = count = 0
        for i in range(x):
            if (isinstance(my_list[i], int)):
                print("{:d}".format(my_list[i]), end='')
                count += 1
        print()
        return count
    except Exception:
        raise
