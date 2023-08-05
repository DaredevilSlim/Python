#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# In a given word you need to check if one symbol goes only right after another.
# Cases you should expect while solving this challenge:
# one of the symbols is not in the given word - your function should return False;
# any symbol appears in a word more than once - use only the first one;
# two symbols are the same - your function should return False;
# the condition is case sensitive, which means 'a' and 'A' are two different symbols.
# Input: Three arguments. The first one is a given string, second is a symbol that should go first, and the third is a
# symbol that should go after the first one.
# Output: A bool.

def goes_after(word: str, first: str, second: str) -> bool:
    first = word.find(first)
    second = word.find(second)
    return first >= 0 and second == first + 1


print(goes_after("world", "w", "o"))      # True
print(goes_after("world", "w", "r"))      # False
print(goes_after("world", "l", "o"))      # False
print(goes_after("panorama", "a", "n"))   # True
print(goes_after("list", "l", "o"))       # False
print(goes_after("", "l", "o"))           # False
print(goes_after("list", "l", "l"))       # False
print(goes_after("world", "d", "w"))      # False
print(goes_after("Almaz", "a", "l"))      # False
print(goes_after('transport', 'r', 't'))  # False
print(goes_after("almaz", "a", "l"))      # True
print(goes_after("almaz", "m", "a"))      # False
