#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 1 ** 2 + 2 ** 2 + 2 ** 2 = 9
def square_sum(numbers: list) -> int:
    result = 0
    for i in numbers:
        result += i ** 2
    return result


print(square_sum([1, 2]))  # 5
print(square_sum([0, 3, 4, 5]))  # 50
print(square_sum([]))  # 0
print(square_sum([-1, -2]))  # 5
print(square_sum([-1, 0, 1]))  # 2
