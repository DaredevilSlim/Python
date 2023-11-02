#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This function should take an list of strings and determine the longest common prefix among all the strings. If there
# is no common prefix, it should return an empty string.
# Input: List of strings (str).
# Output: String (str).
# How it’s used:
# in autocomplete systems to suggest the most likely completion;
# in file systems to suggest directory names based on current input;
# in DNA sequence alignment to identify common substrings.
def longest_prefix(arr: list[str]) -> str:
    m = min(len(i) for i in arr)
    a = [''] * m
    for i in range(m):
        for j in range(len(arr)):
            if a[i] != arr[j][i]:
                a[i] += arr[j][i]
    return ''.join(i for i in a if len(i) == 1)


print(longest_prefix(["flower", "flow", "flight"]))  # "fl"
print(longest_prefix(["dog", "racecar", "car"]))  # ""
print(longest_prefix(["apple", "application", "appetizer"]))  # "app"
print(longest_prefix(["a"]))  # "a"
print(longest_prefix(["", "b"]))  # ""
print(longest_prefix(["same", "same", "same"]))  # "same"
print(longest_prefix(["mismatch", "mister", "miss"]))  # "mis"
print(longest_prefix(["alphabet", "alpha", "alphadog"]))  # "alpha"
print(longest_prefix(["book", "boot", "booster"]))  # "boo"
print(longest_prefix(["short", "shore", "shot"]))  # "sho"
