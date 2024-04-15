#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The easier problem Beat the previous asked you to greedily extract a strictly ascending sequence of integers from the
# given series of digits. For example, for digits equal to "31415926", the list of integers returned should be
# [3, 14, 15, 92], with the last original digit left unused.
# Going somewhat against intuition, the ability to tactically skip some of the digits at will may allow the resulting
# list of integers to contain more elements than the list constructed in the previous greedy fashion. With this
# additional freedom, the example digit string "31415926" would allow the result [3, 4, 5, 9, 26] with one more element
# than the greedily constructed solution.
# Your function should return the length of the longest list of ascending integers that can be extracted from digits.
# Note that you are allowed to skip one or more digits not just between two integers being extracted, but during the
# construction of each such integer.
# Input: String (str).
# Output: Integer (int).
# The mission was taken from Python CCPS 109. It is taught for Ryerson Chang School of Continuing Education by Ilkka
# Kokkarinen
def staircase(digits: str) -> int:
    result = 0
    for i in range(len(digits)):
        n = int(digits[i])
        j = digits.index(digits[i])
        temp = 0
        while j < len(digits[j+1:]) and len(f'{n}') < len(digits[j+1:]):
            if f'{n}' in digits[j+1:]:
                temp += 1
                j = digits[j+1:].index(f'{n}')
            n += 1
    return 0


print(staircase("100123"))  # 4
print(staircase("503715"))  # 4
print(staircase("0425494220946"))  # 6
print(staircase("04414952075836"))  # 7
print(staircase("1234567891011213"))  # 12



