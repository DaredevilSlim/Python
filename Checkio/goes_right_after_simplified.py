#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is the simplified version of Goes Right After mission.
# In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.
# If one of the symbols is not in the given word - your function should return False. If two seeking symbols are the
# same - your function should return False.
# Input: Three arguments. The first one is a given string, second is a symbol that should go first, and the third is a
# symbol that should go after the first one.
# Output: A boolean.
# Preconditions: all symbols are lowercased and unique.
def goes_after(word: str, first: str, second: str) -> bool:
    first = word.find(first)
    second = word.find(second)
    return first >= 0 and second == first + 1


print(goes_after("world", "w", "o"))  # True
print(goes_after("world", "w", "r"))  # False
print(goes_after("world", "l", "o"))  # False
print(goes_after("list", "l", "o"))   # False
print(goes_after("", "l", "o"))       # False
print(goes_after("list", "l", "l"))   # False
print(goes_after("world", "d", "w"))  # False
