#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer n, return a string with n characters such that each character in such string occurs an odd number of
# times.
# The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of
# them.
# Example 1:
# Input: n = 4
# Output: "pppz"
# Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once.
# Note that there are many other valid strings such as "ohhh" and "love".
# Example 2:
# Input: n = 2
# Output: "xy"
# Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid
# strings such as "ag" and "ur".
# Example 3:
# Input: n = 7
# Output: "holasss"
# Constraints:
# 1 <= n <= 500
def generate_the_string(n: int) -> str:
    return 'a' * n if n % 2 else 'a' * (n - 1) + 'b'


print(generate_the_string(4))  # aaab
print(generate_the_string(2))  # ab
print(generate_the_string(7))  # aaaaaaa
