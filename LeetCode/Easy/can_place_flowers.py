#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted
# in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false
# otherwise.
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
# Constraints:
# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    a = 0
    while a < len(flowerbed) - 1:
        if flowerbed[a] == 0 and flowerbed[a+1] == 0:
            if 0 <= a < len(flowerbed)-1:
                flowerbed[a] = 1
            elif a+1 == len(flowerbed):
                flowerbed[a+1] = 1
            n -= 1
        elif flowerbed[a] == 1 and flowerbed[a+1] == 0:
            a += 2
        else:
            a += 1
    print(flowerbed)
    return n == 0


print(can_place_flowers([1, 0, 0, 0, 1], 1))  # True
print(can_place_flowers([0, 0, 1, 0, 1], 1))  # True
print(can_place_flowers([1, 0, 0, 0, 1, 0, 0], 2))  # True
print(can_place_flowers([0, 0, 1, 0, 0], 2))  # True
print(can_place_flowers([1, 0, 0, 0, 1], 2))  # False
print(can_place_flowers([1, 0, 0, 0, 0, 1], 2))  # False
print(can_place_flowers([0, 1, 0, 1, 0], 1))  # False

