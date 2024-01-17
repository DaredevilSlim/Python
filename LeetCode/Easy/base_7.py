#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer num, return a string of its base 7 representation.
# Example 1:
# Input: num = 100
# Output: "202"
# Example 2:
# Input: num = -7
# Output: "-10"
# Constraints:
# -107 <= num <= 107
def convert_to_base7(num: int) -> str:
    if num == 0:
        return '0'
    n = abs(num)
    s = ''
    while n > 0:
        s = f'{n % 7}' + s
        n = n // 7
    return ('-' if num < 0 else '') + s


print(convert_to_base7(100))  # '202'
print(convert_to_base7(-7))  # '-10'
