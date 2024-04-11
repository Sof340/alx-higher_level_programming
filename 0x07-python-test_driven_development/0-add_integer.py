#!/usr/bin/python3
'''
    module that adds two numbers
    Args:
        a, b: integers
'''


def add_integer(a, b=98):
    '''
        Function that adds two integers
    '''
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    elif isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return a + b
