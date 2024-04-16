#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer.
# A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the
# character 'a'.
# Each second, you may perform one of the following operations:
# Move the pointer one character counterclockwise or clockwise.
# Type the character the pointer is currently on.
# Given a string word, return the minimum number of seconds to type out the characters in word.
# Example 1:
# Input: word = 'abc'
# Output: 5
# Explanation: 
# The characters are printed as follows:
# - Type the character 'a' in 1 second since the pointer is initially on 'a'.
# - Move the pointer clockwise to 'b' in 1 second.
# - Type the character 'b' in 1 second.
# - Move the pointer clockwise to 'c' in 1 second.
# - Type the character 'c' in 1 second.
# Example 2:
# Input: word = 'bza'
# Output: 7
# Explanation:
# The characters are printed as follows:
# - Move the pointer clockwise to 'b' in 1 second.
# - Type the character 'b' in 1 second.
# - Move the pointer counterclockwise to 'z' in 2 seconds.
# - Type the character 'z' in 1 second.
# - Move the pointer clockwise to 'a' in 1 second.
# - Type the character 'a' in 1 second.
# Example 3:
# Input: word = 'zjpc'
# Output: 34
# Explanation:
# The characters are printed as follows:
# - Move the pointer counterclockwise to 'z' in 1 second.
# - Type the character 'z' in 1 second.
# - Move the pointer clockwise to 'j' in 10 seconds.
# - Type the character 'j' in 1 second.
# - Move the pointer clockwise to 'p' in 6 seconds.
# - Type the character 'p' in 1 second.
# - Move the pointer counterclockwise to 'c' in 13 seconds.
# - Type the character 'c' in 1 second.
# Constraints:
# 1 <= word.length <= 100
# word consists of lowercase English letters.
def min_time_to_type(word: str) -> int:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    a = alphabet.index(word[0])
    b = min(a - 0, 25 - a + 25 - 0)
    result = b + 1
    i = 1
    while i < len(word):
        c = alphabet.index(word[i])
        print(f'before: a = {a}, c = {c}, result = {result}')
        b = min(abs(a - c), 25 - a + c)
        print(f'b = {b}')
        result += b + 1
        a = c
        print(f'after: a = {a}, c = {c}, result = {result}')
        i += 1
    return result


# print(min_time_to_type('abc'))  # 5
print(min_time_to_type('bza'))  # 7
# print(min_time_to_type('zjpc'))  # 34
