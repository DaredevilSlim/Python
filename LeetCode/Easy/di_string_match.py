#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of
# length n where:
# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, 
# return any of them.
# Example 1:
# Input: s = "IDID"
# Output: [0, 4, 1, 3, 2]
# Example 2:
# Input: s = "III"
# Output: [0, 1, 2, 3]
# Example 3:
# Input: s = "DDI"
# Output: [3, 2, 0, 1]
# Constraints:
# 1 <= s.length <= 105
# s[i] is either 'I' or 'D'.
def di_string_match(s: str) -> list[int]:
    i = 0
    d = len(s)
    j = 0
    result = []
    while i < d:
        if s[j] == 'D':
            result.append(d)
            d -= 1
        else:
            result.append(i)
            i += 1
        j += 1
    return result + [d if s[-1] == 'D' else i]


print(di_string_match('IDID'))  # [0, 4, 1, 3, 2]
print(di_string_match('III'))  # [0, 1, 2, 3]
print(di_string_match('DDI'))  # [3, 2, 0, 1]
