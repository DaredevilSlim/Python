#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The goal is to create a function of two inputs number and power, that "raises" the number up to power (ie multiplies
# number by itself power times).
# Note: math.pow and some others math functions are disabled on final tests.
def number_to_pwr(number: int, p: int) -> int:
    result = 1
    for i in range(p):
        result *= number
    return result


print(number_to_pwr(4, 2))  # 16
print(number_to_pwr(10, 4))  # 10000
print(number_to_pwr(10, 0))  # 1

