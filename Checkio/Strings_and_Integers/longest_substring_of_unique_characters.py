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
    for i in range(len(s)):
        for j in range(len(s)):
            if len(set(s[i:j+1])) == len(s[i:j+1]) > a:
                a += 1
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
