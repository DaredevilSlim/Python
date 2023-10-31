#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This function should take a non-negative integer as an input and return the factorial of that number. The factorial of
# a non-negative integer n is the product of all positive integers less than or equal to n .
# Input: Integer (int).
# Output: Integer (int).
# How it’s used:
# in mathematical applications to calculate permutations and combinations;
# in algorithms to solve problems related to counting arrangements.
# Precondition:
# n ∈ N₀
def factorial(n: int) -> int:
    a = 1
    for i in range(n, 0, -1):
        a *= i
    return a


print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(5))  # 120
print(factorial(10))  # 3628800
print(factorial(15))  # 1307674368000
