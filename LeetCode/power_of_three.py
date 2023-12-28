#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.
# Example 1:
# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:
# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:
# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
# Constraints:
# -231 <= n <= 231 - 1
def is_power_of_three(n: int) -> bool:
    while n > 3:
        n /= 3
    return n == 1 or n == 3


print(is_power_of_three(27))  # True
print(is_power_of_three(2))  # False
print(is_power_of_three(-1))  # False
print(is_power_of_three(0))  # False
print(is_power_of_three(9))  # True
print(is_power_of_three(1))  # True
print(is_power_of_three(19684))  # False
