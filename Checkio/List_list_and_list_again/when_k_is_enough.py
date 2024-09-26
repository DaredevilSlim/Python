#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Iterable, Any

# Given a list of items, some of which may be duplicated, create and return a new Iterable that is otherwise the same as
# items, but only up to k occurrences of each element are kept, and all occurrences of that element after those first k
# are discarded. Note also the counterintuitive but still completely legitimate edge case of k == 0 that has a well
# defined answer of an empty list!
# Input: A list and an integer.
# Output: List or another Iterable (tuple, iterator, generator).
# Examples:
# This task is taken from the course CCPS 109 Computer Science I, as taught by Ilkka Kokkarinen.
def remove_after_kth(items: list[Any], k: int) -> Iterable[Any]:
    new_list = []
    for i in set(items):
        item = items.count(i)
        if item >= k:
            item = k
        for j in range(item):
            new_list.append(i)
    return new_list


print(list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)))  # [42, 42, 42]
print(list(remove_after_kth([42, 42, 42, 99, 99, 17], 0)))  # []
print(list(remove_after_kth([1, 1, 1, 2, 2, 2], 5)))  # [1, 1, 1, 2, 2, 2]
print(list(remove_after_kth(['tom', 42, 'bob', 'bob', 99, 'bob', 'tom', 'tom', 99], 2)))  # ['tom', 42, 'bob', 'bob', 99, 'tom', 99]
