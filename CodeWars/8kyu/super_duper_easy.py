#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/55a5bfaa756cfede78000026
# Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should
# return "Error".
def problem(a: int) -> int:
    if type(a) is str:
        return 'Error'
    return a * 50 + 6


print(problem('hello'))  # 'Error'
print(problem(1))  # 56
