#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
# Example 1:
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15
# Example 2:
# Input: n = 4421
# Output: 21
# Explanation:
# Product of digits = 4 * 4 * 2 * 1 = 32
# Sum of digits = 4 + 4 + 2 + 1 = 11
# Result = 32 - 11 = 21
# Constraints:
# 1 <= n <= 10^5
def subtract_product_and_sum(n: int) -> int:
    n = str(n)
    i = 1
    t = int(n[0])
    p = t
    s = t
    while i < len(n):
        t = int(n[i])
        p *= t
        s += t
        i += 1
    return p - s


print(subtract_product_and_sum(234))  # 15
print(subtract_product_and_sum(4421))  # 21
