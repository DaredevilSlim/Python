#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable

# Create and return a new Iterable that contains the same elements as the given list items, but with the reversed order
# of the elements inside every maximal strictly ascending subsequence. This function should not modify the contents of
# the original list.
# Input: List of integers (int).
# Output: List or another Iterable (tuple, iterator, generator) of integers (int).
# How it is used: (math is used everywhere)
# Precondition: given sequence includes only integers.


'''def reverse_ascending(items: list[int]) -> Iterable[int]:
    if not items or len(items) == 1:
        return items
    new = []
    a = 0
    b = 1
    c = 0
    while a < (len(items) - 1):
        if items[a] >= items[b]:
            new += sorted(items[c:b])[::-1]
            c = b
        a += 1
        b += 1
        if b == len(items):
            new += sorted(items[c:])[::-1]
    return new'''


def reverse_ascending(items: list[int]) -> Iterable[int]:
    if not items or len(items) == 1:
        return items
    new = []
    a = 0
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            new += sorted(items[a:i + 1])[::-1]
            a = i + 1
        if i + 2 == len(items):
            new += sorted(items[a:])[::-1]
    return new


print(list(reverse_ascending([1, 2, 3, 4, 5])))               # [5, 4, 3, 2, 1]
print(list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])))  # [10, 7, 5, 4, 8, 7, 2, 3, 1,]
print(list(reverse_ascending([5, 4, 3, 2, 1])))               # [5, 4, 3, 2, 1]
print(list(reverse_ascending([])))                            # []
print(list(reverse_ascending([1])))                           # [1]
print(list(reverse_ascending([1, 1])))                        # [1, 1]
print(list(reverse_ascending([1, 1, 2])))                     # [1, 2, 1]
print(list(reverse_ascending([1, 2, 2, 3])))                  # [2, 1, 3, 2]
print(list(reverse_ascending([1, 2, 3, 4, 4, 3, 2, 1])))      # [4, 3, 2, 1, 4, 3, 2, 1]
print(list(reverse_ascending([4, 3, 2, 1, 1, 2, 3, 4])))      # [4, 3, 2, 1, 4, 3, 2, 1]
print(list(reverse_ascending([1, 2, 3, 4, 1, 2, 3, 4])))      # [4, 3, 2, 1, 4, 3, 2, 1]
