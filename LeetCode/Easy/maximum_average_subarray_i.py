#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.
# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000
# Constraints:
# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104
def find_max_average(nums: list[int], k: int) -> float:
    if len(nums) <= 4:
        return sum(nums) / k
    nums_list = list()
    a = 0
    b = k
    while b < len(nums) + 1:
        nums_list.append(sum(nums[a:b]) / k)
        a += 1
        b += 1
    return max(nums_list)


print(find_max_average([1, 12, -5, -6, 50, 3], 4))  # 12.75000
print(find_max_average([5], 1))  # 5.00000
print(find_max_average([0, 1, 1, 3, 3], 4))  # 12.75000
print(find_max_average([0, 1, 1, 3, 3], 4))  # 12.75000
