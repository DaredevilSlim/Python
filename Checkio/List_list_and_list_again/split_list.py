#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Any, Iterable

# You have to split a given list into two lists inside an Iterable. If input sequence has an odd amount of elements,
# then the first list inside result Iterable should have more elements. If input sequence has no elements, then two
# empty lists inside result Iterable should be returned.
# Input: A list.
# Output: An Iterable of two lists.


def split_list(items: list[Any]) -> Iterable[list[Any]]:
    len_items = len(items)
    a = len_items - (len_items // 2)
    return [items[:a], items[a:]]


print(list(split_list([1, 2, 3, 4, 5, 6])))  # [[1, 2, 3], [4, 5, 6]]
print(list(split_list([1, 2, 3])))  # [[1, 2], [3]]
print(list(split_list(["banana", "apple", "orange", "cherry", "watermelon"])))  # [["banana", "apple", "orange"],
    # ["cherry", "watermelon"],]
print(list(split_list([1])))  # [[1], []]
print(list(split_list([])))  # [[], []]

