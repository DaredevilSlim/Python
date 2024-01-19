#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different
# size r x c keeping its original data.
# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns
# of the wanted reshaped matrix.
# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as
# they were.
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise,
# output the original matrix.
# Example 1:
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
# Example 2:
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]
# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300
def matrix_reshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    if len(mat[0]) * len(mat) != r * c:
        return mat
    mat_temp = list()
    for i in range(len(mat)):
        mat_temp += mat[i]
    mat_new = list()
    k = 0
    for i in range(r):
        temp = list()
        for j in range(c):
            temp.append(mat_temp[k])
            k += 1
        mat_new.append(temp)
    return mat_new


print(matrix_reshape([[1, 2], [3, 4]], 1, 4))  # [[1, 2, 3, 4]]
print(matrix_reshape([[1, 2], [3, 4]], 2, 4))  # [[1,2], [3,4]]
print(matrix_reshape([[1, 2], [3, 4]], 4, 1))  # [[1], [2], [3], [4]]
