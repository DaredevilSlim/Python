#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
def longest_common_prefix(strs: list[str]) -> str:
    m = min(len(i) for i in strs)
    a = [''] * m
    for i in range(m):
        for j in range(len(strs)):
            if a[i] != strs[j][i]:
                a[i] += strs[j][i]
    i = 0
    new = ''
    while i < len(a) and len(a[i]) == 1:
        new += a[i]
        i += 1
    return new


print(longest_common_prefix(["flower", "flow", "flight"]))  # "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))  # ""
print(longest_common_prefix([""]))  # ""
print(longest_common_prefix(["cir", "car"]))  # "c"
