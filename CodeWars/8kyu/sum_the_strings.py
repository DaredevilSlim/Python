#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
# Notes:
# If either input is an empty string, consider it as zero.
# Inputs and the expected output will never exceed the signed 32-bit integer limit (2^31 - 1)
def sum_str(a: str, b: str) -> str:
    if not a and not b:
        return '0'
    if not a:
        return b
    if not b:
        return a
    return str(eval(f'{a} + {b}'))


print(sum_str('4', '5'))  # '9'
print(sum_str('34', '5'))  # '39'
print(sum_str('9', ''))  # '9'
print(sum_str('', '9'))  # '9'
print(sum_str('', ''))  # '0'
