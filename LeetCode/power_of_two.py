#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.
# Example 1:
# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:
# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:
# Input: n = 3
# Output: false
# Constraints:
# -231 <= n <= 231 - 1
def is_power_of_two(n: int) -> bool:
    while n > 2:
        n /= 2
    return n == 1 or n == 2


print(is_power_of_two(1))  # True
print(is_power_of_two(2))  # True
print(is_power_of_two(3))  # False
