#!/usr/bin/python3
import hidden_4


def print_compiled_words():
    words = dir(hidden_4)
    to_print = []
    for i in range(len(words)):
        k = words[i]
        if (k[0] != '_'):
            to_print.append(k)
    print(to_print)


if __name__ == "__main__":
    print_compiled_words()
