#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that
# |nums[i] - nums[j]| == k.
# The value of |x| is defined as:
# x if x >= 0.
# -x if x < 0.
# Example 1:
# Input: nums = [1, 2, 2, 1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1, 2, 2, 1]
# - [1, 2, 2, 1]
# - [1, 2, 2, 1]
# - [1, 2, 2, 1]
# Example 2:
# Input: nums = [1, 3], k = 3
# Output: 0
# Explanation: There are no pairs with an absolute difference of 3.
# Example 3:
# Input: nums = [3, 2, 1, 5, 4], k = 2
# Output: 3
# Explanation: The pairs with an absolute difference of 2 are:
# - [3, 2, 1, 5, 4]
# - [3, 2, 1, 5, 4]
# - [3, 2, 1, 5, 4]
# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 1 <= k <= 99
def count_k_difference(nums: list[int], k: int) -> int:
    nums = sorted(nums)
    count = 0
    temp = 0
    for i in range(len(nums) - 1):
        if nums[i] == nums[i - 1]:
            count += temp
            continue
        temp = 0
        target = nums[i] + k
        for j in range(i + 1, len(nums)):
            if target > nums[j]:
                continue
            elif target == nums[j]:
                temp += 1
            else:
                break
        count += temp
    return count


print(count_k_difference([1, 2, 2, 1], 1))  # 4
print(count_k_difference([1, 3], 3))  # 0
print(count_k_difference([3, 2, 1, 5, 4], 2))  # 3
print(count_k_difference([7, 7, 8, 3, 1, 2, 7, 2, 9, 5], 6))  # 6
