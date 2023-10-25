#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This function should take a string as an input and return the count of vowels (a, e, i, o, u) in the string.
# The function should be case-insensitive.
# Input: String (str).
# Output: Integer (int).
# How it’s used:
# in natural language processing tasks, like text analysis and statistics;
# in text-based games or learning applications, for instance, to calculate the difficulty level of a word or phrase.
# Preconditions:
# text ∈ string;
# length(text) >= 0.
def count_vowels(text: str) -> int:
    return sum(1 for i in text if i.lower() in ['a', 'e', 'i', 'o', 'u'])


print(count_vowels("hello"))  # 2
print(count_vowels("openai"))  # 4
print(count_vowels("typescript"))  # 2
print(count_vowels("a"))  # 1
print(count_vowels("b"))  # 0
print(count_vowels("aeiou"))  # 5
print(count_vowels("AEIOU"))  # 5
print(count_vowels("The quick brown fox"))  # 5
print(count_vowels("Jumps over the lazy dog"))  # 6
print(count_vowels(""))  # 0
