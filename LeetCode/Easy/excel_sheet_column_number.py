#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding
# column number.
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
# Input: columnTitle = "A"
# Output: 1
# Example 2:
# Input: columnTitle = "AB"
# Output: 28
# Example 3:
# Input: columnTitle = "ZY"
# Output: 701
# Constraints:
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].
def title_to_number(column_title: str) -> int:
    d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
         'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
         'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    a = 0
    for i in column_title[:-1]:
        a += d[i]
        a *= 26
    return a + d[column_title[-1]]


print(title_to_number('ETXU'))  # 102045
print(title_to_number('ODA'))  # 10245
print(title_to_number('DDE'))  # 2813
print(title_to_number('FXSHRXW'))  # 2147483647
print(title_to_number('A'))  # 1
print(title_to_number('AB'))  # 28
print(title_to_number('AZ'))  # 52
print(title_to_number('BZ'))  # 78
print(title_to_number('ZY'))  # 701
print(title_to_number('AAZ'))  # 728
