#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it -
# function should return False.
# Input: A string (str).
# Output: A logic value (bool).
# Precondition: a-z, A-Z, 1-9 and spaces.
# Taken from mission All Upper I
def is_all_upper(text: str) -> bool:
    text = text.replace(' ', '')
    return False if text == '' or text.isdigit() else text == text.upper()


print(is_all_upper("ALL UPPER"))              # True
print(is_all_upper("all lower"))              # False
print(is_all_upper("mixed UPPER and lower"))  # False
print(is_all_upper(""))                       # False
print(is_all_upper('     '))                  # False
