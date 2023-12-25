#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    ds = dict()
    dt = dict()
    for i, j in zip(s, t):
        if i not in ds:
            ds[i] = 1
        elif i in ds:
            ds[i] += 1
        if j not in dt:
            dt[j] = 1
        elif j in dt:
            dt[j] += 1
    return ds == dt


print(is_anagram('anagram', 'nagaram'))  # True
print(is_anagram('rat', 'car'))  # False
print(is_anagram('aacc', 'cacc'))  # False
