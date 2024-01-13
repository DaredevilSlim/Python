#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s
# is 3.
# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2
# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
def find_max_consecutive_ones(nums: list[int]) -> int:
    return len(max(''.join(map(str, nums)).split('0')))


print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))  # 3
print(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]))  # 2
