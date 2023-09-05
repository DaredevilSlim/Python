#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# You are given a string, where all letters are of same case. This string could include adjacent letters - two the same
# letters together ("aa", "bb" etc). Your task in this mission is to remove both these letters. If after removing one
# pair a new appears - remove it as well! Each such pair should be removed from string until no one remains. Good luck!
# Input: String (str).
# Output: String (str).
def adjacent_letters(line: str) -> str:
    a = 0
    while a < len(line) - 1:
        line, a = (line[:a] + line[a+2:], 0) if line[a] == line[a+1] else (line, a + 1)
    return line


print(adjacent_letters("adjacent_letters"))  # "adjacent_lrs"
print(adjacent_letters(""))  # ""
print(adjacent_letters("aaa"))  # "a"
print(adjacent_letters("ABBA"))  # ""
print(adjacent_letters("abcdefghhgfedcba"))  # ""
