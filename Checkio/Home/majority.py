#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# We have a list of booleans. Let's check if the majority of elements are True.
# Some cases worth mentioning: 1) an empty list should return False; 2) if True-s and False-s have an equal amount,
# function should return False.
# Input: A list of booleans.
# Output: A Boolean.
def is_majority(items: list[bool]) -> bool:
    return items.count(True) > items.count(False)


print(is_majority([True, True, False, True, False]))   # True
print(is_majority([True, True, False]))                # True
print(is_majority([True, True, False, False]))         # False
print(is_majority([True, True, False, False, False]))  # False
print(is_majority([False]))                            # False
print(is_majority([True]))                             # True
print(is_majority([]))                                 # False
