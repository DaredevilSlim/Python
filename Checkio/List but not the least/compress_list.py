#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable

# A given sequence should be "compressed" in a way so, instead of two (or more) equal elements, staying one after
# another, there should be only one in the result sequence.
# Input: List.
# Output: "Compressed" List or another Iterable (tuple, iterator, generator).


def compress(items: list[int]) -> Iterable[int]:
    if not items:
        return items
    new = [items[0]]
    for i in items:
        if i != new[-1]:
            new.append(i)
    return new


print(list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])))     # [5, 4, 5, 6, 5, 7, 8, 0,]
print(list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])))              # [1, 2, 1]
print(list(compress([7, 7])))                                      # [7]
print(list(compress([])))                                          # []
print(list(compress([1, 2, 3, 4])))                                # [1, 2, 3, 4]
print(list(compress([9, 9, 9, 9, 9, 9, 9])))                       # [9]
print(list(compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9])))  # [9, 0, 9]
