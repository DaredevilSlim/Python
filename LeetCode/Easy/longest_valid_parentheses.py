#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed)
# parentheses substring.
# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:
# Input: s = ""
# Output: 0
# Constraints:
# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.
def longest_valid_parentheses(s: str) -> int:
    a = 0
    b = 0
    c = s
    d = len(c)
    while a < len(s) // 2:
        c = c.replace('()', '', 1)
        if len(c) < d:
            d = len(c)
            b += 2
        a += 1
    return b


print(longest_valid_parentheses('()(()'))  # 2
'''
print(longest_valid_parentheses('()()(()'))  # 4
print(longest_valid_parentheses('()(()()()'))  # 6
print(longest_valid_parentheses(')))((('))  # 0
print(longest_valid_parentheses(')()())'))  # 4
print(longest_valid_parentheses('(()'))  # 2
print(longest_valid_parentheses(''))  # 0
print(longest_valid_parentheses('()(())'))  # 6
print(longest_valid_parentheses('(()()())'))  # 8
print(longest_valid_parentheses('((((()))))'))  # 10
print(longest_valid_parentheses('()((((()))))()'))  # 14
print(longest_valid_parentheses('(()((((()))))())'))  # 16
'''
