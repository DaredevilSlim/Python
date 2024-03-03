#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The array-form of an integer num is an array representing its digits in left to right order.
# For example, for num = 1321, the array form is [1, 3, 2, 1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
# Example 1:
# Input: num = [1, 2, 0, 0], k = 34
# Output: [1, 2, 3, 4]
# Explanation: 1200 + 34 = 1234
# Example 2:
# Input: num = [2, 7, 4], k = 181
# Output: [4, 5, 5]
# Explanation: 274 + 181 = 455
# Example 3:
# Input: num = [2, 1, 5], k = 806
# Output: [1, 0, 2, 1]
# Explanation: 215 + 806 = 1021
# Constraints:
# 1 <= num.length <= 104
# 0 <= num[i] <= 9
# num does not contain any leading zeros except for the zero itself.
# 1 <= k <= 104
def add_to_array_form(num: list[int], k: int) -> list[int]:
    k_list = [int(i) for i in str(k)][::-1]
    r_num = num[::-1]
    i = 0
    t = 0
    print(f'{k_list[i]} + {r_num[i]} + {t} = {k_list[i] + r_num[i] + t}')
    while r_num[i] + t < 10 or i < len(k_list):
        s = r_num[i] + t
        if s > 10:
            t = s - 10
            r_num[i] = 0
        else:
            r_num[i] = s
        i += 1
    return r_num[::-1]


print(add_to_array_form([1, 2, 0, 0], 34))  # [1, 2, 3, 4]
print(add_to_array_form([2, 7, 4], 181))  # [4, 5, 5]
print(add_to_array_form([2, 1, 5], 806))  # [1, 0, 2, 1]
print(add_to_array_form([1, 2, 0, 0, 9, 9], 34))  # [1, 2, 0, 1, 3, 3]
print(add_to_array_form([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1))  # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
