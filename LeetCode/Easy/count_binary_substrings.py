#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all
# the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.
# Example 1:
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10",
# "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:
# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
# Constraints:
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.
def count_binary_substrings(s: str) -> int:
    if len(s) <= 1:
        return 0
    s_list = s.replace('01', '0 1').replace('10', '1 0').split()
    i = 1
    count = 0
    while i < len(s_list):
        count += min(len(s_list[i-1]), len(s_list[i]))
        i += 1
    return count


print(count_binary_substrings('00110011'))  # 6
print(count_binary_substrings('10101'))  # 4
print(count_binary_substrings('000111'))  # 3
print(count_binary_substrings('11100'))  # 2
print(count_binary_substrings('00011100'))  # 5



