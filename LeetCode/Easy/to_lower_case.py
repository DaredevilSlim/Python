#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
# Example 1:
# Input: s = "Hello"
# Output: "hello"
# Example 2:
# Input: s = "here"
# Output: "here"
# Example 3:
# Input: s = "LOVELY"
# Output: "lovely"
# Constraints:
# 1 <= s.length <= 100
# s consists of printable ASCII characters.
def to_lower_case(s: str) -> str:
    if s.islower():
        return s
    for i in range(len(s)):
        if s[i].isupper():
            s = s[:i] + chr(ord(s[i]) + 32) + s[i+1:]
    return s


print(to_lower_case('Hello'))  # hello
print(to_lower_case('here'))  # here
print(to_lower_case('LOVELY'))  # lovely
