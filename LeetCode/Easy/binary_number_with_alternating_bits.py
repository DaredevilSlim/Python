#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have
# different values.
# Example 1:
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
# Example 2:
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
# Example 3:
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
# Constraints:
# 1 <= n <= 231 - 1
def has_alternating_bits(n: int) -> bool:
    binary = str(bin(n))[2:]
    i = 1
    while i < len(binary) and binary[i-1] != binary[i]:
        i += 1
    return i == len(binary)


print(has_alternating_bits(5))  # True
print(has_alternating_bits(7))  # False
print(has_alternating_bits(4))  # False
print(has_alternating_bits(11))  # False
