#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of
# the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to
# k characters, then reverse the first k characters and leave the other as original.
# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"
# Constraints:
# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 104
def reverse_str(s: str, k: int) -> str:
    for i in range(len(s)):
        if i % (2 * k) == 0:
            s = s[:i] + s[i:i + k][::-1] + s[i + k:]
    return s


print(reverse_str('abcdefg', 2))  # 'bacdfeg'
print(reverse_str('abcd', 2))  # 'bacd'
