#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# -109 <= matrix[i][j] <= 109
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    transpose = [[0] * len(matrix)] * len(matrix[0])
    print(transpose)
    for i in range(len(matrix)):
        print(f'i = {i}')
        for j in range(i+1, len(matrix)):
            print(f'j = {j}')
            transpose[j][i] = matrix[i][j]
    return transpose


print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(transpose([[1, 2, 3], [4, 5, 6]]))  # [[1, 4], [2, 5], [3, 6]]
