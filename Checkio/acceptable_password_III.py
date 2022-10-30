#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# In this mission you need to create a password verification function.
# The verification conditions are:
# the length should be bigger than 6;
# should contain at least one digit, but cannot consist of just digits.
# Input: A string.
# Output: A bool.
# Examples:
# assert is_acceptable_password("short") == False
# assert is_acceptable_password("muchlonger") == False
# assert is_acceptable_password("ashort") == False
# assert is_acceptable_password("muchlonger5") == True
# How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.

def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and any(i.isdigit() for i in password) and any(i.isalpha() for i in password)


print(is_acceptable_password("short"))        # False
print(is_acceptable_password("muchlonger"))   # True
print(is_acceptable_password("ashort"))       # False
print(is_acceptable_password("muchlonger5"))  # True
print(is_acceptable_password("sh5"))          # False
print(is_acceptable_password("1234567"))      # False
