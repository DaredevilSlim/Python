#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
# The test cases are generated so that a unique mapping will always exist.
# Example 1:
# Input: s = '10#11#12'
# Output: 'jkab'
# Explanation: 'j' -> '10#' , 'k' -> '11#' , 'a' -> '1' , 'b' -> '2'.
# Example 2:
# Input: s = '1326#'
# Output: 'acz'
# Constraints:
# 1 <= s.length <= 1000
# s consists of digits and the '#' letter.
# s will be a valid string such that mapping is always possible.
def freq_alphabets(s: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(9, len(alphabet)):
        s = s.replace(f'{i+1}#', f'{alphabet[i]}')
    for i in range(9):
        s = s.replace(f'{i+1}', f'{alphabet[i]}')
    return s


print(freq_alphabets('10#11#12'))  # 'jkab'
print(freq_alphabets('1326#'))  # 'acz'
