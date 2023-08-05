#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable

# Not all of the elements are important. What you need to do here is to remove all of the elements after the given one
# from sequence.
# For illustration, we have a sequence [1, 2, 3, 4, 5] and we need to remove all the elements that go after 3 - which
# are 4 and 5.
# We have two edge cases here:
# if a cutting element cannot be found, then the sequence shouldn't be changed;
# if the sequence is empty, then it should remains empty.
# Input: List of integers (int).
# Output: List or other Iterable (tuple, iterator, generator ...) of integers (int).


def remove_all_after(items: list[int], border: int) -> Iterable[int]:
    return items if border not in items else items[:items.index(border) + 1]


print(list(remove_all_after([1, 2, 3, 4, 5], 3)))              # [1, 2, 3]
print(list(remove_all_after([1, 1, 2, 2, 3, 3], 2)))           # [1, 1, 2]
print(list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)))        # [1, 1, 2]
print(list(remove_all_after([1, 1, 5, 6, 7], 2)))              # [1, 1, 5, 6, 7]
print(list(remove_all_after([], 0)))                           # []
print(list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)))  # [7]
