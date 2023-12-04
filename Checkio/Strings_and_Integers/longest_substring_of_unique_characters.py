#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string, find the length of the longest substring without repeating characters.
# Input: String (str).
# Output: Integer (int).
# How it’s used:
# data validation for passwords to ensure the inclusion of a sufficiently long sequence of non-repeated characters;
# text analysis, especially for cryptography and coding patterns;
# identifying unique patterns in a sequence.
def longest_substr(s: str) -> int:
    a = 0
    b = ''
    for i in s:
        b = (b[b.index(i) + 1:] if i in b else b) + i
        if len(b) > a:
            a = len(b)
    return a


print(longest_substr('anviaj'))  # 5
print(longest_substr("dvdf"))  # 3
print(longest_substr('ohomm'))  # 3
print(longest_substr("abcabcbb"))  # 3
print(longest_substr("bbbbb"))  # 1
print(longest_substr("pwwkew"))  # 3
print(longest_substr("abcdef"))  # 6
print(longest_substr(""))  # 0
print(longest_substr("au"))  # 2
