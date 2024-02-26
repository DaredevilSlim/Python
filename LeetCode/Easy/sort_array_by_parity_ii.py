#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.
# Example 1:
# Input: nums = [4, 2, 5, 7]
# Output: [4, 5, 2, 7]
# Explanation: [4, 7, 2, 5], [2, 5, 4, 7], [2, 7, 4, 5] would also have been accepted.
# Example 2:
# Input: nums = [2, 3]
# Output: [2, 3]
# Constraints:
# 2 <= nums.length <= 2 * 104
# nums.length is even.
# Half of the integers in nums are even.
# 0 <= nums[i] <= 1000
def sort_array_by_parity_ii(nums: list[int]) -> list[int]:
    i = 0
    odd = []
    even = []
    result = []
    while i < len(nums):
        if nums[i] % 2 != 0:
            odd += [nums[i]]
        else:
            even += [nums[i]]
        i += 1
    for i, j in zip(even, odd):
        result += [i, j]
    return result


print(sort_array_by_parity_ii([4, 2, 5, 7]))  # [4, 5, 2, 7]
print(sort_array_by_parity_ii([2, 3]))  # [2, 3]
print(sort_array_by_parity_ii([3, 1, 4, 2]))  # [2, 1, 4, 3]
print(sort_array_by_parity_ii([888, 505, 627, 846]))  # [888, 505, 846, 627]
