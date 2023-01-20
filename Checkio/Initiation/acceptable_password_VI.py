#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# In this mission you need to create a password verification function.
# The verification conditions are:
# the length should be bigger than 6;
# should contain at least one digit, but cannot consist of just digits.
# if the password is longer than 9 - previous rule (about one digit), is not required.
# a string should not contain the word "password" in any case.
# should contain at least 3 different letters (or digits) even if it is longer than 10
# Input: A string.
# Output: A bool.
# How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.

def is_acceptable_password(password: str) -> bool:
    if 'password' in password.lower() and len(set(password)) >= 3:
        return False
    return ((len(password) > 6
             and not password.isdigit()
             and not password.isalpha())
            or len(password) > 9) \
           and len(set(password)) >= 3


print(is_acceptable_password("short"))                  # False
print(is_acceptable_password("muchlonger"))             # True
print(is_acceptable_password("ashort"))                 # False
print(is_acceptable_password("muchlonger5"))            # True
print(is_acceptable_password("sh5"))                    # False
print(is_acceptable_password("1234567"))                # False
print(is_acceptable_password("12345678910"))            # True
print(is_acceptable_password("password12345"))          # False
print(is_acceptable_password("PASSWORD12345"))          # False
print(is_acceptable_password("pass1234word"))           # True
print(is_acceptable_password("aaaaaa1"))                # False
print(is_acceptable_password("aaaaaabbbbb"))            # False
print(is_acceptable_password("aaaaaabb1"))              # True
print(is_acceptable_password("abc1"))                   # False
print(is_acceptable_password("abbcc12"))                # True
print(is_acceptable_password("aaaaaaabbaaaaaaaab"))     # False
