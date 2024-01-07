#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1
# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.
def first_uniq_char(s: str) -> int:
    di = dict()
    for i in range(len(s)):
        if s[i] not in s[i+1:] and s[i] not in di:
            return i
        if s[i] not in di:
            di[s[i]] = 1
    return -1


print(first_uniq_char('leetcode'))  # 0
print(first_uniq_char('loveleetcode'))  # 2
print(first_uniq_char('aabb'))  # -1
