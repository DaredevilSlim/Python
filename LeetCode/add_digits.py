#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
# Example 1:
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.
# Example 2:
# Input: num = 0
# Output: 0
# Constraints:
# 0 <= num <= 231 - 1
def add_digits(num: int) -> int:
    while len(str(num)) > 1:
        num = sum(int(i) for i in str(num))
    return num


print(add_digits(38))  # 2
print(add_digits(1234567890))  # 9
print(add_digits(0))  # 0
