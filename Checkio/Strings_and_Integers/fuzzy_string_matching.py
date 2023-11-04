#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given two strings and a permissible number of character differences, determine if the strings can be considered
# approximately equal.
# Input: Three arguments: two strings (str) and one integer (int).
# Output: Logic value (bool).
# How it’s used:
# spell-checking algorithms where slight differences can be ignored;
# searching algorithms in databases to find entries that closely match the query;
# DNA sequence matching where certain differences might be allowed.
# Precondition:
# 0 <= threshold <= max(len(str1), len(str2)).
def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    return False if (abs(len(str1) - len(str2)) + sum(1 for i, j in zip(str1, str2) if i != j)) > threshold else True


print(fuzzy_string_match("apple", "appel", 2))  # True
print(fuzzy_string_match("apple", "bpple", 1))  # True
print(fuzzy_string_match("apple", "bpple", 0))  # False
print(fuzzy_string_match("apple", "apples", 1))  # True
print(fuzzy_string_match("apple", "bpples", 2))  # True
print(fuzzy_string_match("apple", "apxle", 1))  # True
print(fuzzy_string_match("apple", "pxxli", 3))  # False
