#!/usr/bin/python3
'''
A module that prints the content of a file.
'''


def read_file(filename=""):
    '''
    A function that prints the content of a file to the stdout
    Arguements:
        filename: the name of the file (the path)
    '''
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
    f.close()
