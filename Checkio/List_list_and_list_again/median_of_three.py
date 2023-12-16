#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Iterable

# Given an iterable of ints , create and return a new iterable whose first two elements are the same as in items, after
# which each element equals the median element in the list of the three elements from the original list. This list of
# three ends on the current position, first two elements are going just before the third element.
# Wait...You don't know what the "median" is? Go check out the separate "Median" mission on CheckiO.
# Input: Iterable of ints.
# Output: Iterable of ints.
# The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School of Continuing
# Education by Ilkka Kokkarinen


def median_three(els: Iterable[int]) -> Iterable[int]:
    return els if len(els) <= 2 else els[:2] + [sorted(els[i-2:i+1])[1] for i in range(2, len(els))]


print(median_three([1, 2, 3, 4, 5, 6, 7]))  # [1, 2, 2, 3, 4, 5, 6]
print(median_three([1]))  # [1]


