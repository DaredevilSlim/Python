#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. For example,
# 28 is a perfect number because its divisors are 1, 2, 4, 7, and 14, and their sum is 28.
# Input: Integer (int).
# Output: Logic value (bool).
# How it’s used: perfect numbers have a historical significance in number theory and have been studied in various
# mathematical and mystical contexts. This function could be useful in mathematical research, cryptography, or just
# general problem-solving.
# Precondition:
# 1 <= n <= 108
def is_perfect(n: int) -> bool:
    # your code here
    return False


print(is_perfect(6))  # True
print(is_perfect(2))  # False
print(is_perfect(28))  # True
print(is_perfect(20))  # False
print(is_perfect(496))  # True
print(is_perfect(30))  # False
print(is_perfect(8128))  # True
print(is_perfect(100))  # False
print(is_perfect(500))  # False
print(is_perfect(1000))  # False
