#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
# signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21
# Constraints:
# -231 <= x <= 231 - 1
def reverse(x: int) -> int:
    a = int(str(abs(x))[::-1])
    return 0 if a > 2147483647 else a if x > 0 else -a


print(reverse(123))  # 321
print(reverse(9646324351))  # 1534236469
print(reverse(1534236469))  # 0
print(reverse(7463847412))  # 2147483647
print(reverse(1563847412))  # 0
print(reverse(-123))  # -321
print(reverse(120))  # 21
