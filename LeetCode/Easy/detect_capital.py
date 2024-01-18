#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.
# Example 1:
# Input: word = "USA"
# Output: true
# Example 2:
# Input: word = "FlaG"
# Output: false
# Constraints:
# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.
def detect_capital_use(word: str) -> bool:
    if word.isupper() or word.islower() or word[0].isupper() and word[1:].islower():
        return True
    return False


print(detect_capital_use('USA'))  # True
print(detect_capital_use('FlaG'))  # False
print(detect_capital_use('leetcode'))  # True
print(detect_capital_use('Google'))  # True
