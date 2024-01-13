#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.
# Example 1:
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.
# Example 2:
# Input: x = 3, y = 1
# Output: 1
# Constraints:
# 0 <= x, y <= 231 - 1
def hamming_distance(x: int, y: int) -> int:
    return sum(1 for i, j in zip(f'{x:032b}', f'{y:032b}') if i != j)


print(hamming_distance(1, 4))  # 2
print(hamming_distance(3, 1))  # 1
