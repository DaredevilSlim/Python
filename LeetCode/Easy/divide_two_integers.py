#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be
# truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:
# [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the
# quotient is strictly less than -231, then return -231.
# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
# Constraints:
# -231 <= dividend, divisor <= 231 - 1
# divisor != 0
def divide(dividend: int, divisor: int) -> int:
    a = 0
    if abs(dividend) == abs(divisor):
        a = 1
    elif divisor == 1:
        if dividend > 0:
            a = dividend
        elif dividend < 0:
            a = abs(dividend)
    elif divisor == -1:
        if dividend < 0:
            a = abs(dividend) - 1
    elif dividend == 0:
        a = 0
    else:
        b = abs(divisor)
        c = b
        while c <= dividend:
            c += b
            a += 1
    return a if (divisor < 0 > dividend) or (divisor > 0 < dividend) else -a


print(divide(10, 3))  # 3
print(divide(7, -3))  # -2
print(divide(1, 1))  # 1
print(divide(-1, 1))  # -1
print(divide(-1, -1))  # 1
print(divide(0, 1))  # 0
'''
print(divide(-2147483648, -1))  # 2147483647
print(divide(-2147483648, 1))  # -2147483648
print(divide(2147483647, 1))  # 2147483647
print(divide(2147483647, 2))  # 2147483647
'''
