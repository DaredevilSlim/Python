#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
# the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
# "abcde" while "aec" is not).
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
def is_subsequence(s: str, t: str) -> bool:
    i = 0
    j = 0
    while i < len(s):
        if s[i] in t[j:]:
            j += t[j:].index(s[i]) + 1
            i += 1
        else:
            return False
    return True


print(is_subsequence('abc', 'ahbgdc'))  # True
print(is_subsequence('axc', 'ahbgdc'))  # False
print(is_subsequence('b', 'c'))  # False
print(is_subsequence('aaaaaa', 'bbaaaa'))  # False
print(is_subsequence('', 'ahbgdc'))  # True
