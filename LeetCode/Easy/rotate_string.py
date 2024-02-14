#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.
# Example 1:
# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:
# Input: s = "abcde", goal = "abced"
# Output: false
# Constraints:
# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.
def rotate_string(s: str, goal: str) -> bool:
    i = 0
    while s != goal:
        if i > len(goal):
            return False
        s = s[1:] + s[0]
        i += 1
    return True


print(rotate_string('abcde', 'cdeab'))  # True
print(rotate_string('abcde', 'abced'))  # False
