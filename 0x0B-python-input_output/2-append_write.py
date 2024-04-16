#!/usr/bin/python3
'''
A module that appends text to a file.
'''


def append_write(filename="", text=""):
    '''
    a function that appends a string at the end of a text file
    and returns the number of characters added.
    Arguments:
        filename: path of the file.
        text: string to write into the file.
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        d = f.write(text)
    f.close()
    return d
