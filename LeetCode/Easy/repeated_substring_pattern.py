#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the
# substring together.
# Example 1:
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:
# Input: s = "aba"
# Output: false
# Example 3:
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
# Constraints:
# 1 <= s.length <= 104
# s consists of lowercase English letters.
def repeated_substring_pattern(s: str) -> bool:
    if len(s) <= 1:
        return False
    a = 1
    b = 1
    while b < len(s):
        if s[:a] == s[a:a + b]:
            c = s[:a]
            while len(c) <= len(s):
                if c == s:
                    return True
                c += s[:a]
        a += 1
        b += 1
    return False


print(repeated_substring_pattern('abab'))  # True
print(repeated_substring_pattern('aba'))  # False
print(repeated_substring_pattern('abcabcabcabc'))  # True
print(repeated_substring_pattern('aaaa'))  # True
print(repeated_substring_pattern('a'))  # False
print(repeated_substring_pattern('abaababaab'))  # True
