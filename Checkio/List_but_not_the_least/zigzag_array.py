#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Your function should create a list of lists, that represents a two-dimensional grid with the given number of rows and
# cols.
# This grid should contain integers (int) from start to start + rows * cols - 1 in ascending order, but the elements of
# every odd-index row have to be listed in descending order, so that when read in ascending order, the numbers zigzag
# through the two-dimensional grid.
# Input: Two integers (int) - rows and columns. One optional integer (int) - start.
# Output: List of lists.
def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
    new = [[0 for i in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols) if i % 2 == 0 else range(cols - 1, -1, -1):
            new[i][j] = start
            start += 1
    return new


print(create_zigzag(3, 5))     # [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
print(create_zigzag(5, 1))     # [[1], [2], [3], [4], [5]]
print(create_zigzag(4, 2))     # [[1, 2], [4, 3], [5, 6], [8, 7]]
print(create_zigzag(0, 3))     # []
print(create_zigzag(3, 0))     # [[], [], []]
print(create_zigzag(0, 0))     # []
print(create_zigzag(10, 1))    # [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
print(create_zigzag(3, 3, 5))  # [[5, 6, 7], [10, 9, 8], [11, 12, 13]]
