#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given two binary strings a and b, return their sum as a binary string.
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
def add_binary(a: str, b: str) -> str:
    return f'{int(a, 2) + int(b, 2):b}'


print(add_binary('11', '1'))  # '100'
print(add_binary('1010', '1011'))  # '10101'
