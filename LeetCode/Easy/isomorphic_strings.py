#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
# Input: s = "paper", t = "title"
# Output: true
# Constraints:
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.
def is_isomorphic(s: str, t: str) -> bool:
    s_dict = dict()
    t_dict = dict()
    for i in range(len(s)):
        if s[i] in s_dict:
            s_dict[s[i]] += 1 + i
        else:
            s_dict[s[i]] = 1 + i
    for j in range(len(t)):
        if t[j] in t_dict:
            t_dict[t[j]] += 1 + j
        else:
            t_dict[t[j]] = 1 + j
    return list(s_dict.values()) == list(t_dict.values())


print(is_isomorphic('a', 'a'))  # True
print(is_isomorphic('ab', 'ab'))  # True
print(is_isomorphic('ab', 'ac'))  # True
print(is_isomorphic('egg', 'add'))  # True
print(is_isomorphic('paper', 'title'))  # True
print(is_isomorphic('bbbaaaba', 'aaabbbba'))  # False
print(is_isomorphic('foo', 'bar'))  # False
print(is_isomorphic('papap', 'titii'))  # False
print(is_isomorphic('badc', 'baba'))  # False
print(is_isomorphic('abcdefghijklmnopqrstuvwxyzva', 'abcdefghijklmnopqrstuvwxyzck'))  # False
