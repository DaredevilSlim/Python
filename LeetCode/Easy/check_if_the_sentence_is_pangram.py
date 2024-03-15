#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false
# otherwise.
# Example 1:
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:
# Input: sentence = "leetcode"
# Output: false
# Constraints:
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.
def check_if_pangram(sentence: str) -> bool:
    i = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    while i < len(alphabet) and alphabet[i] in sentence:
        i += 1
    return i == 26


print(check_if_pangram('thequickbrownfoxjumpsoverthelazydog'))  # True
print(check_if_pangram('leetcode'))  # False
