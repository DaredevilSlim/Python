#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable

# Sort the integers in sequence. But the position of zeros should not be changed.
# Input: List of integers (int).
# Output: List or another Iterable (tuple, generator, iterator) of integers (int).
# Precondition:
# All numbers are non-negative.


def except_zero(items: list[int]) -> Iterable[int]:
    new = sorted(items)[items.count(0):]
    [new.insert(i, 0) for i in range(len(items))if items[i] == 0]
    return new


print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))  # [1, 3, 0, 0, 4, 4, 5, 0, 7]
print(list(except_zero([0, 2, 3, 1, 0, 4, 5])))        # [0, 1, 2, 3, 0, 4, 5]
print(list(except_zero([0, 0, 0, 1, 0])))              # [0, 0, 0, 1, 0]
print(list(except_zero([4, 5, 3, 1, 1])))              # [1, 1, 3, 4, 5]
print(list(except_zero([0, 0])))                       # [0, 0]
