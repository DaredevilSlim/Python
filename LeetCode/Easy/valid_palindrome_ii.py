#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# Example 1:
# Input: s = "aba"
# Output: true
# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:
# Input: s = "abc"
# Output: false
# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.
def valid_palindrome(s: str) -> bool:
    len_s = len(s)
    one = 0
    two = len_s - 1
    while one < len_s // 2 and s[one] == s[two]:
        one += 1
        two -= 1
    s_one = s[one:two]
    s_two = s[one + 1:two + 1]
    if s_one == s_one[::-1] or s_two == s_two[::-1]:
        return True
    return False


print(valid_palindrome('aba'))  # True
print(valid_palindrome('abc'))  # False
print(valid_palindrome('abca'))  # True
