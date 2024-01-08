#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that
# can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
def longest_palindrome(s: str) -> int:
    dict_s = dict()
    a = 0
    b = 0
    for i in s:
        if i in dict_s:
            dict_s[i] += 1
        else:
            dict_s[i] = 1
    if len(dict_s) == 1:
        return len(s)
    for j in dict_s:
        if dict_s[j] % 2 == 0:
            a += dict_s[j]
        else:
            a += (dict_s[j] // 2) * 2
            b = 1
    return a + b


print(longest_palindrome('abccccdd'))  # 7
print(longest_palindrome('a'))  # 1
print(longest_palindrome('ccc'))  # 3
print(longest_palindrome('bananas'))  # 5
