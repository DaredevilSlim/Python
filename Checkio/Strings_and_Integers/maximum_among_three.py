#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given three integers, determine which one is the largest.
# Input: Three integers (int).
# Output: Integer (int).
# How it’s used: this function can be used in various algorithms and computations where the highest value among multiple
# options needs to be selected.
# Precondition:
# -109 <= a, b, c <= 109.
def max_of_three(a: int, b: int, c: int) -> int:
    return max(a, b, c)


print(max_of_three(1, 2, 3))  # 3
print(max_of_three(3, 2, 1))  # 3
print(max_of_three(1, 3, 2))  # 3
print(max_of_three(0, 0, 0))  # 0
print(max_of_three(-1, -2, -3))  # -1
print(max_of_three(5, 5, 4))  # 5
print(max_of_three(-5, -5, -6))  # -5
print(max_of_three(10, 9, 10))  # 10
print(max_of_three(123, 456, 789))  # 789
print(max_of_three(789, 123, 456))  # 789
