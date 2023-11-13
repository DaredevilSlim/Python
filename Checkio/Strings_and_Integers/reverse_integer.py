#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Reverse the digits of a given integer. For instance, 1234 should become 4321. For negative integers, the sign should
# remain in the front; e.g., -123 becomes -321.
# Input: Integer (int).
# Output: Integer (int).
# How it’s used: this function can be utilized in various algorithmic challenges, number-based puzzles, and certain
# numerical calculations.
# Precondition:
# −109 ≤ num ≤ 109.
def reverse_digits(num: int) -> int:
    a = int(str(abs(num))[::-1])
    return a if num > 0 else -a


print(reverse_digits(1234))  # 4321
print(reverse_digits(0))  # 0
print(reverse_digits(-123))  # -321
print(reverse_digits(5))  # 5
print(reverse_digits(-9))  # -9
print(reverse_digits(100))  # 1
print(reverse_digits(-100))  # -1
print(reverse_digits(54321))  # 12345
print(reverse_digits(1111))  # 1111
print(reverse_digits(987654321))  # 123456789
