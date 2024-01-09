#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not
# exist, return the maximum number.
# Example 1:
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:
# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.
# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
def third_max(nums: list[int]) -> int:
    nums = sorted(set(nums))
    return min(nums[-3:]) if len(nums) > 2 else max(nums)


print(third_max([3, 2, 1]))  # 1
print(third_max([2, 1]))  # 2
print(third_max([2, 2, 3, 1]))  # 1
print(third_max([1, 2, 2, 5, 3, 5]))  # 2
print(third_max([-1, 2, 3]))  # -1
print(third_max([-4, -5, -3, -2, -1]))  # -3
