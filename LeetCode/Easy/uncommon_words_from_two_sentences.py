#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
# Example 1:
# Input: s1 = 'this apple is sweet', s2 = 'this apple is sour'
# Output: ['sweet','sour']
# Example 2:
# Input: s1 = 'apple apple', s2 = 'banana'
# Output: ['banana']
# Constraints:
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.
def uncommon_from_sentences(s1: str, s2: str) -> list[str]:
    both = (s1 + ' ' + s2).split()
    set_both = set(both)
    result = []
    for i in set_both:
        if both.count(i) == 1:
            result.append(i)
    return result


print(uncommon_from_sentences('this apple is sweet', 'this apple is sour'))  # ['sweet','sour']
print(uncommon_from_sentences('apple apple', 'banana'))  # ['banana']
print(uncommon_from_sentences('d b zu d t', 'udb zu ap'))  # ['b', 't', 'udb', 'ap']
