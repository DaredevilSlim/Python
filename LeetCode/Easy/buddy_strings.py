#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise,
# return false.
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at
# s[i] and s[j].
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
# Example 1:
# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
# Example 2:
# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
# Example 3:
# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
# Constraints:
# 1 <= s.length, goal.length <= 2 * 104
# s and goal consist of lowercase letters.
def buddy_strings(s: str, goal: str) -> bool:
    if len(s) != len(goal) or len(s) <= 1:
        return False
    if s == s[::-1]:
        return True
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            for j in range(i, len(s)):
                if s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:] == goal:
                    return True
    return False


print(buddy_strings('ab', 'ba'))  # True
print(buddy_strings('ab', 'ab'))  # False
print(buddy_strings('aa', 'aa'))  # True
print(buddy_strings('aaab', 'aaab'))  # True
print(buddy_strings('abab', 'baba'))  # False
print(buddy_strings('a', 'a'))  # False
print(buddy_strings('abcd', 'abcd'))  # False
