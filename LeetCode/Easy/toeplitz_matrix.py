#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
# Example 1:
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
# Example 2:
# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99
def is_toeplitz_matrix(matrix: list[list[int]]) -> bool:
    diag_list = [0] * (len(matrix[0]))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            #diag_list[i+j] += matrix[i][j]
            print(f'i = {i}, j = {j}, matrix[i][j] = {matrix[i][j]}')
    return diag_list


print(is_toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))  # True
print(is_toeplitz_matrix([[1, 2], [2, 2]]))  # False
