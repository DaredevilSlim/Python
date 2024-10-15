#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/5641a03210e973055a00000d
# Each number should be formatted that it is rounded to two decimal places. You don't need to check whether the input is
# a valid number because only valid numbers are used in the tests.
# Example:
# 5.5589 is rounded 5.56
# -3.3424 is rounded -3.34
def two_decimal_places(n: float) -> float:
    return float(f'{n:.2f}')


print(two_decimal_places(4.659725356))  # 4.66
print(two_decimal_places(173735326.3783732637948948))  # 173735326.38
print(two_decimal_places(4.653725356))  # 4.65
