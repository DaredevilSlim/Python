#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given a string. Your function should return True if the string is a valid number (contains digits only),
# otherwise - False. Look at the example.
# Input: A string.
# Output: A boolean.
# How it’s used: For checking string values that must contain only digits.
# Precondition: The text contains only letters, digits and whitespace.
def is_number(val: str) -> bool:
    return val.isdigit()


print(is_number("34"))  # True
print(is_number("df"))  # False
print(is_number(""))  # False
print(is_number("a5"))  # False
print(is_number("ITS A NUMBER"))  # False
print(is_number("5a"))  # False
