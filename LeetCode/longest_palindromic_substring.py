#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string s, return the longest palindromic substring in s.
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
'''
def longest_palindrome(s: str) -> str:
    c = ''
    for i in range(len(s)):
        b = ''
        for j in range(i, len(s)):
            b += s[j]
            if b == b[::-1]:
                if len(b) > len(c):
                    c = b
    return c
'''


def longest_palindrome(s: str) -> str:
    if not s or len(s) == 1:
        return s
    a = s[0]
    for i in range(len(s)):
        b = s.rfind(s[i])
        while i < b:
            if s[i:b + 1] == s[i:b + 1][::-1]:
                if len(s[i:b + 1]) > len(a):
                    a = s[i:b + 1]
            b = s[:b].rfind(s[i])
    return a


print(longest_palindrome('babad'))  # 'bab'
print(longest_palindrome('cbbd'))  # 'bb'
print(longest_palindrome('a'))  # 'a'
print(longest_palindrome('ac'))  # 'a'
