#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score = 0
    student = ""
    for k, v in a_dictionary.items():
        if score < v:
            score = v
            student = k
    if student == "":
        return None
    return student
