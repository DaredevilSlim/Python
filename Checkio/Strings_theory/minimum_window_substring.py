#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string line and a pattern pattern, write a function to find the minimum window substring of the line that
# contains at least all the characters of the pattern (may contain other characters also). The order of the characters
# in the line/pattern doesn't matter, but the letter case does.
# Your function should return a tuple of starting and ending indexes of line which form the needed window (right border
# is excluded). If there is no such substring in line to match pattern, return (-1, -1).
# Input: Two strings (str).
# Output: Tuple of two integers (int).
# Precondition: all letters in pattern are unique.
def window(line: str, pattern: str) -> tuple[int, int]:
    result_list = []
    d = dict()
    for i in range(len(line)):
        if line[i] in pattern:
            if line[i] in d:
                d[line[i]] += [i]
            else:
                d[line[i]] = [i]
    print(d)
    return -1, -1


print(window("ADOBECODEBANC", "ABC"))  # (9, 13)
print(window("ab", "a"))  # (0, 1)
print(window("ab", "A"))  # (-1, -1)
print(window("abcdef", "ace"))  # (0, 5)
print(window("MixEdCaSeScRiNgTrIcKy", "cSeR"))  # (8, 12)

