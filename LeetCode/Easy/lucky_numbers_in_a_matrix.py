#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
# Example 1:
# Input: matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 2:
# Input: matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:
# Input: matrix = [[7, 8], [1, 2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= n, m <= 50
# 1 <= matrix[i][j] <= 105.
# All elements in the matrix are distinct.
def lucky_numbers(matrix: list[list[int]]) -> list[int]:
    min_n = [min(i) for i in matrix]
    for i in range(len(matrix[0])):
        max_i = 0
        for j in range(len(matrix)):
            if matrix[j][i] > max_i:
                max_i = matrix[j][i]
        if max_i in min_n:
            return [max_i]


print(lucky_numbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))  # [15]
print(lucky_numbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))  # [12]
print(lucky_numbers([[7, 8], [1, 2]]))  # [7]
