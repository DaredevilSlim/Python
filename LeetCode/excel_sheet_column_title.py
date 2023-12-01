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
    a = ord('A')
    b = ord('Z')
    return b - a


print(convert_to_title(1))  # 'A'
print(convert_to_title(28))  # 'AB'
print(convert_to_title(701))  # 'ZY'
