#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# In this mission you need to create a password verification function.
# The verification conditions are:
# the length should be bigger than 6;
# should contain at least one digit, but cannot consist of just digits.
# if the password is longer than 9 - previous rule (about one digit), is not required.
# Input: A string.
# Output: A bool.
# How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.

def is_acceptable_password(password: str) -> bool:
    return (len(password) > 6 and not password.isdigit() and not password.isalpha()) or len(password) > 9


print(is_acceptable_password("short"))        # False
print(is_acceptable_password("muchlonger"))   # True
print(is_acceptable_password("ashort"))       # False
print(is_acceptable_password("muchlonger5"))  # True
print(is_acceptable_password("sh5"))          # False
print(is_acceptable_password("1234567"))      # False
print(is_acceptable_password("12345678910"))  # True
