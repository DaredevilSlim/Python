#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
# Example 1:
# Input: nums = [1,2,3]
# Output: 6
# Example 2:
# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:
# Input: nums = [-1,-2,-3]
# Output: -6
# Constraints:
# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000
def maximum_product(nums: list[int]) -> int:
    nums = sorted(nums)
    a, b, c = nums[:3]
    d, e, f = nums[-3:]
    return max(a * b * c, a * b * f, a * e * f, d * e * f)


print(maximum_product([1, 2, 3]))  # 6
print(maximum_product([1, 2, 3, 4]))  # 24
print(maximum_product([-1, -2, -3]))  # -6
print(maximum_product([-100, -98, -1, 2, 3, 4]))  # 39200
