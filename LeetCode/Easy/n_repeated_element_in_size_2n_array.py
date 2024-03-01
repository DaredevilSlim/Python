#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given an integer array nums with the following properties:
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.
# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: 3
# Example 2:
# Input: nums = [2, 1, 2, 5, 3, 2]
# Output: 2
# Example 3:
# Input: nums = [5, 1, 5, 2, 5, 3, 5, 4]
# Output: 5
# Constraints:
# 2 <= n <= 5000
# nums.length == 2 * n
# 0 <= nums[i] <= 104
# nums contains n + 1 unique elements and one of them is repeated exactly n times.
def repeated_n_times(nums: list[int]) -> int:
    n = len(nums)
    i = 0
    dict_nums = dict.fromkeys(nums, 0)
    while i < n:
        dict_nums[nums[i]] += 1
        i += 1
    list_keys = list(dict_nums.keys())
    list_values = list(dict_nums.values())
    return list_keys[list_values.index(n // 2)]


print(repeated_n_times([1, 2, 3, 3]))  # 3
print(repeated_n_times([2, 1, 2, 5, 3, 2]))  # 2
print(repeated_n_times([5, 1, 5, 2, 5, 3, 5, 4]))  # 5
