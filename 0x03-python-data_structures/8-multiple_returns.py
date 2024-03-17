#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    return (sentence.count("") - 1, sentence[0])
