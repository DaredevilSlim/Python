#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Determine whether a sequence of elements is ascending such that each of its elements is strictly larger than (and not
# merely equal to) the preceding element. Empty sequence is considered as ascending.
# Input: List with integers (int).
# Output: Logic value (bool).
def is_ascending(items: list[int]) -> bool:
    return not [False for i in range(len(items) - 1) if items[i] >= items[i + 1]]


print(is_ascending([-5, 10, 99, 123456]))   # True
print(is_ascending([99]))                   # True
print(is_ascending([4, 5, 6, 7, 3, 7, 9]))  # False
print(is_ascending([]))                     # True
print(is_ascending([1, 1, 1, 1]))           # False
print(is_ascending([1, 3, 3, 5]))           # False
