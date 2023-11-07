#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Determine the remainder from division of two positive integers.
# Input: Two integers (int): dividend (the number to be divided) and divisor (the number by which division is to be
# performed).
# Output: Integer (int).
# How it’s used: remainder calculations are common in algorithms, especially in modular arithmetic which is frequently
# used in cryptography and computer graphics.
# Precondition:
# dividend, divisor > 0.
def find_remainder(dividend: int, divisor: int) -> int:
    return dividend % divisor


print(find_remainder(10, 3))  # 1
print(find_remainder(14, 4))  # 2
print(find_remainder(27, 4))  # 3
print(find_remainder(10, 5))  # 0
print(find_remainder(10, 1))  # 0
print(find_remainder(5, 7))  # 5
print(find_remainder(7, 5))  # 2

