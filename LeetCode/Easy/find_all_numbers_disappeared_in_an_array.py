#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the
# range [1, n] that do not appear in nums.
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
# Input: nums = [1,1]
# Output: [2]
# Constraints:
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as
# extra space.
def find_disappeared_numbers(nums: list[int]) -> list[int]:
    return list(set([i for i in range(1, len(nums)+1)]).difference(frozenset(nums)))


print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))  # [5, 6]
print(find_disappeared_numbers([1, 1]))  # [2]
print(find_disappeared_numbers([10, 2, 5, 10, 9, 1, 1, 4, 3, 7]))  # [6, 8]
print(find_disappeared_numbers([2, 2]))  # [1]
