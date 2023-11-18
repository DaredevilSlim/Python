#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CheckiO platform has a similar mission Verify Anagrams, but in it you have to determine whether words are anagrams.
# In this mission, the task will be a little different. You are given two strings and need to determine whether you can
# swap two letters in the first string to get the second string. If so (or words are the same) - return True, if not -
# False.
# For example, the string "btry", if we swap y and t, we get "byrt".
# Input: Two strings (str).
# Output: Logic value (bool).
# Preconditions:
# All letters are in lower case;
# Only letters.
def switch_strings(line: str, result: str) -> bool:
    return True if sum(1 for i, j in zip(line, result) if i != j and i in result) == 2 or line == result else False


print(switch_strings("btry", "byrt"))  # True
print(switch_strings("boss", "boss"))  # True
print(switch_strings("solid", "disel"))  # False
print(switch_strings("false", "flaes"))  # False
print(switch_strings("true", "treu"))  # True
print(switch_strings('burx', 'byrt'))  # False

