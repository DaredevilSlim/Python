#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of
# any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as
# nums.
# Example 1:
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation:
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
# Constraints:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.
def find_shortest_sub_array(nums: list[int]) -> int:
    first = dict()
    for i in range(len(nums)):
        if nums[i] not in first:
            first[nums[i]] = [1, i, i]
        else:
            first[nums[i]][0] += 1
            first[nums[i]][2] = i
    final = dict()
    for j in first:
        if first[j][0] not in final:
            final[first[j][0]] = [first[j][2] + 1 - first[j][1]]
        else:
            final[first[j][0]] += [first[j][2] + 1 - first[j][1]]
    return min(final[max(final)])


print(find_shortest_sub_array([1, 2, 2, 3, 1]))  # 2
print(find_shortest_sub_array([1, 2, 2, 3, 1, 4, 2]))  # 6
print(find_shortest_sub_array([1, 5, 2, 3, 5, 4, 5, 6]))  # 6
print(find_shortest_sub_array([10, 9, 9, 9, 10]))  # 3
print(find_shortest_sub_array([1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2]))  # 9
