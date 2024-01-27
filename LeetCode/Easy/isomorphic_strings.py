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
    if s == t:
        return True
    s_list = list(s[0])
    t_list = list(t[0])
    s_index = 0
    t_index = 0
    for i, j in zip(range(1, len(s)), range(1, len(t))):
        if s[i] in s[:i]:
            s_index += s[:i].rindex(s[i])
        if s[i] != s_list[-1][-1]:
            s_list.append(s[i])
        if t[j] in t[:j]:
            t_index += t[:j].rindex(t[j])
        if t[j] != t_list[-1][-1]:
            t_list.append(t[j])
    return len(s_list) == len(t_list) and s_index == t_index


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
