#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false
# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
def is_valid(s: str) -> bool:
    for i in range(len(s) // 2):
        s = s.replace('{}' if '{}' in s else '[]' if '[]' in s else '()', '')
    return len(s) == 0


print(is_valid('()'))  # True
print(is_valid('(){}[]'))  # True
print(is_valid('(]'))  # False
print(is_valid('({[]})'))  # True
