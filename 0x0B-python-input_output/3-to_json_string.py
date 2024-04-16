#!/usr/bin/python3
import json
'''
A module that serializes an obj.
'''


def to_json_string(my_obj):
    '''
    A function that returns an obj input as an str outpt.
    Argument:
        my_obj: the object to serialize.
    '''
    d = json.dumps(my_obj)
    return d
