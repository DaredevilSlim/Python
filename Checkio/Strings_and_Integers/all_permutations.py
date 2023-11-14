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


def string_permutations(s: str) -> Iterable[str]:
    sl = len(s)
    count = 1
    for i in range(sl, 0, -1):
        count *= i
    ls = []
    for i in range(len(s)):
        # a = count // i
        #print('before first', s)
        a = s
        for j in range(count, 1, -1):
            #print('before', a)
            if a not in ls:
                ls.append(a)
            if count % j == 0:
                a = a[:2] + a[2:][::-1]
            else:
                a = a[1:] + a[0]
            print('after', a)
        s = s[-1] + s[:-1][::-1]
        #print('after first', s)
    return sorted(ls)

'''
print(list(string_permutations('abc')))  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

print(list(string_permutations('ab')))  # ['ab', 'ba']
print(list(string_permutations('a')))  # ['a']'''
print(list(string_permutations('abcd')))  #
'''[
    'abcd',
    'abdc',
    'acbd',
    'acdb',
    'adbc',
    'adcb',
    'bacd',
    'badc',
    'bcad',
    'bcda',
    'bdac',
    'bdca',
    'cabd',
    'cadb',
    'cbad',
    'cbda',
    'cdab',
    'cdba',
    'dabc',
    'dacb',
    'dbac',
    'dbca',
    'dcab',
    'dcba',
]'''
