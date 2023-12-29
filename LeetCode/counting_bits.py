#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of
# 1's in the binary representation of i.
# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# Constraints:
# 0 <= n <= 105
def count_bits(n: int) -> list[int]:
    return [bin(i).count('1') for i in range(n+1)]


print(count_bits(2))  # [0, 1, 1]
print(count_bits(5))  # [0, 1, 1, 2, 1, 2]
print(count_bits(6))  # [0, 1, 1, 2, 1, 2, 2]
print(count_bits(7))  # [0, 1, 1, 2, 1, 2, 2, 3]
print(count_bits(8))  # [0, 1, 1, 2, 1, 2, 2, 3, 1]
print(count_bits(9))  # [0, 1, 1, 2, 1, 2, 2, 3, 1, 2]


