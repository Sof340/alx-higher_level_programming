#!/usr/bin/python3
from calculator_1 import mul, div, add, sub
from sys import argv


def calculatrice():
    if (len(argv) != 4):
        print(argv)
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    if (argv[2] != '*' or '/' or '+' or '-'):
        print("Unknown operator. Available operators: +, -, * and /")
        return 1
    a = int(argv[1])
    b = int(argv[3])
    if (argv[2] == '*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif (argv[2] == '/'):
        print("{} / {} = {}".format(a, b, div(a, b)))
    elif (argv[2] == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    else:
        print("{} + {} = {}".format(a, b, add(a, b)))


if __name__ == "__main__":
    calculatrice()
