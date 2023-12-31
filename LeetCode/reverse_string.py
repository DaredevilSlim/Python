#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# Constraints:
# 1 <= s.length <= 105
# s[i] is a printable ascii character.
def reverse_string(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    a = len(s) % 2
    b = len(s) // 2
    c = b - 1
    d = b + 1 if a else b
    while c >= 0:
        s[c], s[d] = s[d], s[c]
        c -= 1
        d += 1


print(reverse_string(["h", "e", "l", "l", "o"]))  # ["o", "l", "l", "e", "h"]
print(reverse_string(["H", "a", "n", "n", "a", "h"]))  # ["h", "a", "n", "n", "a", "H"]
