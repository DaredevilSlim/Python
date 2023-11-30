#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
def generate(num_rows: int) -> list[list[int]]:
    if not num_rows:
        return [[]]
    num = []
    for i in range(num_rows):
        num.append([1] * (i+1))
        if i > 1:
            for j in range(i):
                if 0 < j < len(num[i]):
                    num[i][j] = num[i-1][j-1] + num[i-1][j]
    return num


def get_row(row_index: int) -> list[int]:
    num_rows = row_index + 1
    num = []
    for i in range(num_rows):
        num.append([1] * (i + 1))
        if i > 1:
            for j in range(i):
                if 0 < j < len(num[i]):
                    num[i][j] = num[i - 1][j - 1] + num[i - 1][j]
    return num[row_index]


print(get_row(3))  # [1, 3, 3, 1]
print(get_row(0))  # [1]
print(get_row(1))  # [1, 1]
print(get_row(6))  # [1, 6, 15, 20, 15, 6, 1]
