#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd
# integers.
# Return any array that satisfies this condition.
# Example 1:
# Input: nums = [3, 1, 2, 4]
# Output: [2, 4, 3, 1]
# Explanation: The outputs [4, 2, 3, 1], [2, 4, 1, 3], and [4, 2, 1, 3] would also be accepted.
# Example 2:
# Input: nums = [0]
# Output: [0]
# Constraints:
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000
# def sort_array_by_parity(nums: list[int]) -> list[int]:
#     return sorted(nums, key=lambda x: x % 2 != 0)
def sort_array_by_parity(nums: list[int]) -> list[int]:
    i = 0
    odd = []
    even = []
    while i < len(nums):
        if nums[i] % 2 != 0:
            odd += [nums[i]]
        else:
            even += [nums[i]]
        i += 1
    return odd + even


print(sort_array_by_parity([3, 1, 2, 4]))  # [2, 4, 3, 1]
print(sort_array_by_parity([0]))  # [0]
