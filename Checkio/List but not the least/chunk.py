#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable

# You have a lot of work to do, so you might want to split it into smaller pieces. This way you'll know which piece
# you'll do on Monday, which will be for Tuesday and so on.
# Split list into smaller lists of the same size (chunks). The last chunk can be smaller than the default chunk-size. If
# the given list is empty, then you shouldn't have any chunks at all.
# Input: Two arguments. List and chunk size as integer (int).
# Output: List or another Iterable (tuple, generator, iterator) with chunked lists.
# Precondition: chunk-size > 0


def chunking_by(items: list[int], size: int) -> Iterable[list[int]]:
    if not items:
        return []
    if len(items) <= size:
        return [items]
    return [items[i * size:(i + 1) * size] for i in range(len(items) // size + len(items) % size)]


print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))  # [[5, 4, 7], [3, 4, 5], [4]]
print(list(chunking_by([3, 4, 5], 1)))  # [[3], [4], [5]]
print(list(chunking_by([5, 4], 7)))  # [[5, 4]]
print(list(chunking_by([], 3)))  # []
print(list(chunking_by([4, 4, 4, 4], 4)))  # [[4, 4, 4, 4]]
