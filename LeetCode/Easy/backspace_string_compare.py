#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a
# backspace character.
# Note that after backspacing an empty text, the text will continue empty.
# Example 1:
# Input: s = 'ab#c', t = 'ad#c'
# Output: true
# Explanation: Both s and t become 'ac'.
# Example 2:
# Input: s = 'ab##', t = 'c#d#'
# Output: true
# Explanation: Both s and t become ''.
# Example 3:
# Input: s = 'a#c', t = 'b'
# Output: false
# Explanation: s becomes 'c' while t becomes 'b'.
# Constraints:
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
# Follow up: Can you solve it in O(n) time and O(1) space?
def backspace_compare(s: str, t: str) -> bool:
    def string_exec(string: str) -> str:
        i = 0
        while i < len(string):
            if string[i] == '#':
                if i > 0:
                    string = string[:i - 1] + string[i + 1:]
                    i -= 1
                else:
                    string = string[i + 1:]
                    i = 0
            else:
                i += 1
        return string
    s = string_exec(s)
    t = string_exec(t)
    return s == t


print(backspace_compare('ab#c', 'ad#c'))  # True
print(backspace_compare('ab##', 'c#d#'))  # True
print(backspace_compare('a#c', 'b'))  # False
print(backspace_compare('a##c', '#a#c'))  # True
print(backspace_compare('y#fo##f', 'y#f#o##f'))  # True
print(backspace_compare('hd#dp#czsp#####', 'hd#dp#czsp#######'))  # False
