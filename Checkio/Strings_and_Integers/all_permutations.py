#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable

# Given a string, return all possible permutations of its characters, sorted alphabetically.
# Input: String (str).
# Output: Iterable of strings (str).
# How it’s used:
# puzzles and games like Scrabble where word combinations matter;
# cryptography to test possible keys given a set of characters;
# data analysis in genetics for possible gene combinations.


def count_permutation(s: str) -> int:
    a = 1
    for i in range(len(s), 1, -1):
        a *= i
    return a


def string_permutations(s: str) -> Iterable[str]:
    count = count_permutation(s)
    print(count)
    return []


print(list(string_permutations("ab")))  # ["ab", "ba"]
print(list(string_permutations("abc")))  # ["abc", "acb", "bac", "bca", "cab", "cba"]
print(list(string_permutations("a")))  # ["a"]
print(list(string_permutations("abcd")))  #
'''[
    "abcd",
    "abdc",
    "acbd",
    "acdb",
    "adbc",
    "adcb",
    "bacd",
    "badc",
    "bcad",
    "bcda",
    "bdac",
    "bdca",
    "cabd",
    "cadb",
    "cbad",
    "cbda",
    "cdab",
    "cdba",
    "dabc",
    "dacb",
    "dbac",
    "dbca",
    "dcab",
    "dcba",
]'''
