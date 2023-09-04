#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given a list of integers. Your function should return the number of elements, which are not at their places as
# if the list would be sorted ascending. For example, for the sequence [1, 1, 4, 2, 1, 3] the result is 3, since
# elements at indexes 2, 4, 5 (remember about 0-based indexing in Python) are not at their places as in the same
# sequence sorted ascending - [1, 1, 1, 2, 3, 4].
# Input: List of integers (int).
# Output: Integer (int).
def not_order(data: list[int]) -> int:
    a = 0
    for i in range(len(data) - 1):
        if data[i] > data[i+1]:
            a += 1
            data = data[:i] + data[i:] + [data[i]]
    return 0 if not data else a


print(not_order([1, 1, 4, 2, 1, 3]))  # 3
print(not_order([]))  # 0
print(not_order([1, 1, 1, 1, 1]))  # 0
print(not_order([1, 2, 3, 4, 5]))  # 0
