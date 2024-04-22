#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present
# in at least two out of the three arrays. You may return the values in any order.
# Example 1:
# Input: nums1 = [1, 1, 3, 2], nums2 = [2, 3], nums3 = [3]
# Output: [3, 2]
# Explanation: The values that are present in at least two arrays are:
# - 3, in all three arrays.
# - 2, in nums1 and nums2.
# Example 2:
# Input: nums1 = [3, 1], nums2 = [2, 3], nums3 = [1, 2]
# Output: [2, 3, 1]
# Explanation: The values that are present in at least two arrays are:
# - 2, in nums2 and nums3.
# - 3, in nums1 and nums2.
# - 1, in nums1 and nums3.
# Example 3:
# Input: nums1 = [1, 2, 2], nums2 = [4, 3, 3], nums3 = [5]
# Output: []
# Explanation: No value is present in at least two arrays.
# Constraints:
# 1 <= nums1.length, nums2.length, nums3.length <= 100
# 1 <= nums1[i], nums2[j], nums3[k] <= 100
def two_out_of_three(nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
    a = set(nums1) & set(nums2)
    b = set(nums1) & set(nums3)
    c = set(nums3) & set(nums2)
    return list(a | b | c)


print(two_out_of_three([1, 1, 3, 2], [2, 3], [3]))  # [3, 2]
print(two_out_of_three([3, 1], [2, 3], [1, 2]))  # [2, 3, 1]
print(two_out_of_three([1, 2, 2], [4, 3, 3], [5]))  # []
