#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given a sequence of integers, which are elements of arithmetic progression - the difference between the
# consecutive elements is constant. But this sequence is unsorted and one element is missing...good luck!
# Input: List of integers (int).
# Output: An integer (int).
# Preconditions:
# length of sequence > 2;
# missing element is always between two elements in sequence.
def missing_number(items: list[int]) -> int:
    lis = sorted(items)
    res = 0
    for i in range(len(items) - 2):
        if lis[i+1] - lis[i] > lis[i+2] - lis[i+1]:
            res = lis[i] + (lis[i+1] - lis[i]) // 2
    return res


print(missing_number([1, 4, 2, 5]))         # 3
print(missing_number([2, 6, 8]))            # 4
print(missing_number([5, 25, 30, 20, 15]))  # 10
