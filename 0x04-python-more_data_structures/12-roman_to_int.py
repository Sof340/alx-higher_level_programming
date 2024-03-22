#!/usr/bin/python3
def roman_to_int(roman_string):
    if ((roman_string is str) or roman_string is None):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    for i in range(len(roman_string)):
        if roman_string[i] in roman:
            if (roman_string[i] == 'I' and
                    i + 1 < len(roman_string) and
                    roman_string[i + 1] != 'I'):
                number -= 1
            elif (roman_string[i] == 'X' and
                    i + 1 < len(roman_string) and
                    roman_string[i + 1] == 'C'):
                number -= 10
            else:
                number += roman[roman_string[i]]
    return number
