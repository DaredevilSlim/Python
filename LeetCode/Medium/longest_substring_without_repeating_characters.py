#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
def length_of_longest_substring(s: str) -> int:
    a = 0
    b = ''
    for i in s:
        b = (b[b.index(i) + 1:] if i in b else b) + i
        if len(b) > a:
            a = len(b)
    return a


print(length_of_longest_substring('dvdf'))  # 3
print(length_of_longest_substring(' '))  # 1
print(length_of_longest_substring('abcabcbb'))  # 3
print(length_of_longest_substring('bbbbb'))  # 1
print(length_of_longest_substring('pwwkew'))  # 3
