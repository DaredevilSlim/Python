#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you
# have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also
# jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0
# Constraints:
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.
def num_jewels_in_stones(jewels: str, stones: str) -> int:
    summa = 0
    for stone in stones:
        if stone in jewels:
            summa += 1
    return summa


print(num_jewels_in_stones('aA', 'aAAbbbb'))  # 3
print(num_jewels_in_stones('z', 'ZZ'))  # 0
