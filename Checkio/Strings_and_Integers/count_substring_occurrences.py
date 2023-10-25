#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This function should take a main string and a substring as inputs and return the number of occurrences of the
# substring within the main string. It should not be case-sensitive and may overlap.
# Input: Two strings (str).
# Output: Integer (int).
# How it’s used:
# in a word processing software to highlight or replace all occurrences of a particular word or phrase;
# in website scraping to count the number of times a particular keyword appears;
# in an analytics application to analyze the frequency of certain words or phrases in a body of text.
# Preconditions:
# both inputs should be strings: mainStr ∈ string and subStr ∈ string;
# the main string can have any length, including zero: 0 <= length(mainStr) <= N;
# the substring should not be an empty string: length(subStr) > 0.
def count_occurrences(main_str: str, sub_str: str) -> int:
    return main_str.lower().count(sub_str.lower())


print(count_occurrences("hello world hello", "hello"))  # 2
print(count_occurrences("Hello World hello", "hello"))  # 2
print(count_occurrences("hello", "world"))  # 0
print(count_occurrences("hello world hello world hello", "world"))  # 2
print(count_occurrences("HELLO", "hello"))  # 1
print(count_occurrences("HELLO WORLD", "WORLD"))  # 1
print(count_occurrences("hello world hello", "o w"))  # 1
print(count_occurrences("apple apple apple", "apple"))  # 3
print(count_occurrences("apple Apple apple", "apple"))  # 3
print(count_occurrences("apple", "APPLE"))  # 1
print(count_occurrences('appleappleapple', 'appleapple'))  # 2
