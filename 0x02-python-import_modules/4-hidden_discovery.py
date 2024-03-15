#!/usr/bin/python3
import hidden_4


def print_compiled_words():
    words = dir(hidden_4)
    to_print = []
    for i in range(len(words)):
        k = words[i]
        if (k[0] != '_'):
            to_print.append(k)
    for i in range(len(to_print)):
        print(to_print[i])


if __name__ == "__main__":
    print_compiled_words()
