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
    result = 0
    i = 0
    a = 0
    while i < len(word):
        b = alphabet.index(word[i])
        one = abs(a - b)
        two = (25 - b + a) + 1
        three = ((b + a) % 25) + 1
        print(f'b = {b}, one = {one}, two = {two}, three = {three}, word[i] = {word[i]}')
        c = min(one, two, three)
        result += c + 1
        # print(f'b = {b}, c = {c}, result = {result}, word[i] = {word[i]}')
        a = b
        i += 1
    return result


print(min_time_to_type('abc'))  # 5
print(min_time_to_type('bza'))  # 7
print(min_time_to_type('zjpc'))  # 34
print(min_time_to_type('pdy'))  # 31
print(min_time_to_type('evbedrhwy'))  # 31
