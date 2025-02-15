#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/57f780909f7e8e3183000078
# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
def grow(arr: list) -> int:
    result = 1
    for i in arr:
        result *= i
    return result


print(grow([1, 2, 3]))  # 6
print(grow([4, 1, 1, 1, 4]))  # 16
print(grow([2, 2, 2, 2, 2, 2]))  # 64
