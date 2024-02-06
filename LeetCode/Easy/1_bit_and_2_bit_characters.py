#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# We have two special characters:
# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
# Example 1:
# Input: bits = [1,0,0]
# Output: true
# Explanation: The only way to decode it is two-bit character and one-bit character.
# So the last character is one-bit character.
# Example 2:
# Input: bits = [1,1,1,0]
# Output: false
# Explanation: The only way to decode it is two-bit character and two-bit character.
# So the last character is not one-bit character.
# Constraints:
# 1 <= bits.length <= 1000
# bits[i] is either 0 or 1.
def is_one_bit_character(bits: list[int]) -> bool:
    bits = bits[-2::-1]
    i = 0
    while i < len(bits) and bits[i] == 1:
        i += 1
    return i % 2 == 0


print(is_one_bit_character([1, 0, 0]))  # True
print(is_one_bit_character([0, 0, 0]))  # True
print(is_one_bit_character([0]))  # True
print(is_one_bit_character([1, 1, 0]))  # True
print(is_one_bit_character([0, 1, 1, 0]))  # True
print(is_one_bit_character([0, 1, 0]))  # False
print(is_one_bit_character([1, 1, 1, 0]))  # False
print(is_one_bit_character([0, 1, 1, 1, 0]))  # False
