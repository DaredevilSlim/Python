#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
# elements.
# Note that you must do this in-place without making a copy of the array.
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
def move_zeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    a = 0
    b = len(nums)
    while a < b:
        if nums[a] == 0:
            nums.pop(a)
            nums.append(0)
            b -= 1
        else:
            a += 1
    # return nums


print(move_zeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(move_zeroes([0]))  # [0]
print(move_zeroes([0, 0, 1]))  # [1, 0, 0]
