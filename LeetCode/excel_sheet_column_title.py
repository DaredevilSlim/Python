#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
# Example 1:
# Input: columnNumber = 1
# Output: "A"
# Example 2:
# Input: columnNumber = 28
# Output: "AB"
# Example 3:
# Input: columnNumber = 701
# Output: "ZY"
# Constraints:
# 1 <= columnNumber <= 231 - 1
def convert_to_title(column_number: int) -> str:
    d = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
         11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
         20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
    s = ''
    while column_number > 0:
        if column_number < 27:
            s += d[column_number]
            column_number = 0
        else:
            t = column_number // 26
            s += d[t]
            column_number = column_number % 26
    return s


print(convert_to_title(1))  # 'A'
print(convert_to_title(28))  # 'AB'
print(convert_to_title(701))  # 'ZY'
print(705 // 26, 705 % 26)
#print(convert_to_title(2147483647))  # 'ZY'
