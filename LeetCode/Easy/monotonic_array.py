#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if
# for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.
# Example 1:
# Input: nums = [1, 2, 2, 3]
# Output: true
# Example 2:
# Input: nums = [6, 5, 4, 4]
# Output: true
# Example 3:
# Input: nums = [1, 3, 2]
# Output: false
# Constraints:
# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105
def is_monotonic(nums: list[int]) -> bool:
    if len(nums) == 1:
        return True
    i = 1
    if nums.index(min(nums)) != 0:
        nums.reverse()
    while i < len(nums):
        if nums[i - 1] - nums[i] <= 0:
            i += 1
        else:
            return False
    return True


print(is_monotonic([1, 1, 1]))  # True
print(is_monotonic([9]))  # True
print(is_monotonic([1, 2, 2, 3]))  # True
print(is_monotonic([1, 2, 4, 5]))  # True
print(is_monotonic([6, 5, 4, 4]))  # True
print(is_monotonic([1, 1, 0]))  # True
print(is_monotonic([1, 3, 2]))  # False
print(is_monotonic([2, 2, 2, 1, 4, 5]))  # False
