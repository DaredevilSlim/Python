#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
# Return the number of special letters in word.
# Example 1:
# Input: word = 'aaAbcBC'
# Output: 3
# Explanation:
# The special characters in word are 'a', 'b', and 'c'.
# Example 2:
# Input: word = 'abc'
# Output: 0
# Explanation:
# No character in word appears in uppercase.
# Example 3:
# Input: word = 'abBCab'
# Output: 1
# Explanation:
# The only special character in word is 'b'.
# Constraints:
# 1 <= word.length <= 50
# word consists of only lowercase and uppercase English letters.
def number_of_special_chars(word: str) -> int:
    return sum(1 for i in set(i for i in word if i.islower()) if i.upper() in word)


print(number_of_special_chars('aaAbcBC'))  # 3
print(number_of_special_chars('abc'))  # 0
print(number_of_special_chars('abBCab'))  # 1
print(number_of_special_chars('BBbab'))  # 1
