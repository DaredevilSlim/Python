#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and
# remove the letter at that index from word so that the frequency of every letter present in word is equal.
# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false
# otherwise.
# Note:
# The frequency of a letter x is the number of times it occurs in the string.
# You must remove exactly one letter and cannot choose to do nothing.
# Example 1:
# Input: word = "abcc"
# Output: true
# Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
# Example 2:
# Input: word = "aazz"
# Output: false
# Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice
# versa. It is impossible to make all present letters have equal frequency.
# Constraints:
#
# 2 <= word.length <= 100
# word consists of lowercase English letters only.
def equal_frequency(word: str) -> bool:
    word_dict = dict.fromkeys(word)
    for letter in word_dict.keys():
        word_dict[letter] = word.count(letter)
    max_val = max(word_dict.values())
    min_val = min(word_dict.values())
    max_count = list(word_dict.values()).count(max_val)
    min_count = list(word_dict.values()).count(min_val)
    word_count = len(set(list(word_dict.values())))
    if max_val == 1 or len(set(word)) == 1:
        return True
    if max_val - 1 == min_val and (max_count == 1 or min_count == min_val == 1):
        return True
    if word_count <= 2 and max_val > min_val == min_count == 1:
        return True
    return False


print(equal_frequency('zz'))  # True
print(equal_frequency('bac'))  # True
print(equal_frequency('abcc'))  # True
print(equal_frequency('abbcc'))  # True
print(equal_frequency('cccaa'))  # True
print(equal_frequency('cccd'))  # True
print(equal_frequency('abbbccc'))  # True
print(equal_frequency('aazz'))  # False
print(equal_frequency('cbccca'))  # False
print(equal_frequency('ddaccb'))  # False
print(equal_frequency('babbdd'))  # False
print(equal_frequency('ceeeec'))  # False
print(equal_frequency('aaaabbbbccc'))  # False
