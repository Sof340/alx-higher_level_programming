#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    weight = 0
    sum_ = 0
    result = 0
    for i in range(len(my_list)):
        weight += my_list[i][1]
        sum_ += (my_list[i][0] * my_list[i][1])
    result = sum_ / weight
    return result
