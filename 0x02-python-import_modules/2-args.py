#!/usr/bin/python3
from sys import argv


def argument_output():
    if (len(argv) == 1):
        print("0 arguments.")
    elif (len(argv) == 2):
        print("1 argument")
        print("1 : {}".format(argv[1]))
    else:
        i = 1
        print("{} arguments:".format(len(argv) - 1))
        while (i < len(argv)):
            print("{}: {}".format(i, argv[i]))
            i += 1


if __name__ == "__main__":
    argument_output()
