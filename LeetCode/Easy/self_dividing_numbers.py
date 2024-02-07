#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
# Example 1:
# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
# Example 2:
# Input: left = 47, right = 85
# Output: [48,55,66,77]
# Constraints:
# 1 <= left <= right <= 104
def self_dividing_numbers(left: int, right: int) -> list[int]:
    list_numbers = list()
    for i in range(left, right+1):
        number = list(set(str(i)))
        if '0' not in number:
            len_number = len(number)
            index = 0
            while index < len_number and i % int(number[index]) == 0:
                index += 1
            if len_number == index:
                list_numbers.append(i)
    return list_numbers


print(self_dividing_numbers(1, 22))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
print(self_dividing_numbers(47, 85))  # [48, 55, 66, 77]
