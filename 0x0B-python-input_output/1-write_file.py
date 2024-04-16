#!/usr/bin/python3
'''
A module that write into a file no matter what.
'''


def write_file(filename="", text=""):
    '''
    function that writes a string to a text file.
    Arguments:
        filename: the path of the file.
        text: the text to write into the file
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        d = f.write(text)
    f.close()
    return d
