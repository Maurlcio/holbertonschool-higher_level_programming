#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i = 0
    for j in range(len(roman_string)):
        if j > 0 and romans[roman_string[j]] > romans[roman_string[j - 1]]:
            i += romans[roman_string[j]] - 2 * romans[roman_string[j - 1]]
        else:
            i += romans[roman_string[j]]
    return i
