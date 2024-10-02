#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one
# pivot index for the given input.
# Example 1:
# Input: n = 8
# Output: 6
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
# Example 2:
# Input: n = 1
# Output: 1
# Explanation: 1 is the pivot integer since: 1 = 1.
# Example 3:
# Input: n = 4
# Output: -1
# Explanation: It can be proved that no such integer exist.
# Constraints:
# 1 <= n <= 1000
def pivot_integer(n: int) -> int:
    one = [1]
    for i in range(2, n + 1):
        one.append(one[-1] + i)
    two = [n]
    for j in range(n - 1, 0, -1):
        value = two[-1] + j
        two.append(value)
    print(f'one = {one}, two = {two}')
    for k in range(1, n):
        if one[k] == two[k]:
            return k

    return -1


print(pivot_integer(8))  # 6
print(pivot_integer(1))  # 1
print(pivot_integer(4))  # -1
