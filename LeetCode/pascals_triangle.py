#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
def generate(num_rows: int) -> list[list[int]]:
    num = []
    for i in range(num_rows):
        num.append([1] * (i+1))
        if i > 1:
            for j in range(i):
                if 0 < j < len(num[i]):
                    num[i][j] = num[i-1][j-1] + num[i-1][j]
    return [[]] if not num_rows else num


print(generate(0))  # [[0]]
print(generate(5))  # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(generate(1))  # [[1]]
print(generate(6))  # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
