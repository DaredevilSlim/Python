#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent
# if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.
# Example 1:
# Input: allowed = 'ab', words = ['ad', 'bd', 'aaab', 'baa', 'badab']
# Output: 2
# Explanation: Strings 'aaab' and 'baa' are consistent since they only contain characters 'a' and 'b'.
# Example 2:
# Input: allowed = 'abc', words = ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
# Output: 7
# Explanation: All strings are consistent.
# Example 3:
# Input: allowed = 'cad', words = ['cc', 'acd', 'b', 'ba', 'bac', 'bad', 'ac', 'd']
# Output: 4
# Explanation: Strings 'cc', 'acd', 'ac', and 'd' are consistent.
# Constraints:
# 1 <= words.length <= 104
# 1 <= allowed.length <= 26
# 1 <= words[i].length <= 10
# The characters in allowed are distinct.
# words[i] and allowed contain only lowercase English letters.
def count_consistent_strings(allowed: str, words: list[str]) -> int:
    allowed = set(allowed)
    result = 0
    for i in words:
        if not (set(i) - allowed):
            result += 1
    return result


print(count_consistent_strings('ab', ['ad', 'bd', 'aaab', 'baa', 'badab']))  # 2
print(count_consistent_strings('abc', ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']))  # 7
print(count_consistent_strings('cad', ['cc', 'acd', 'b', 'ba', 'bac', 'bad', 'ac', 'd']))  # 4
