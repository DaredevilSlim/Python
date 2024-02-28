#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Example 1:
# Input: arr = [2, 1]
# Output: false
# Example 2:
# Input: arr = [3, 5, 5]
# Output: false
# Example 3:
# Input: arr = [0, 3, 2, 1]
# Output: true
# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104
def valid_mountain_array(arr: list[int]) -> bool:
    if len(arr) == 1 or arr[0] > arr[1]:
        return False
    i = 1
    while i < len(arr) and arr[i-1] < arr[i]:
        i += 1
    if i == len(arr):
        return False
    while i < len(arr) and arr[i-1] > arr[i]:
        i += 1
    return i == len(arr)


print(valid_mountain_array([2]))  # False
print(valid_mountain_array([2, 1]))  # False
print(valid_mountain_array([3, 5, 5]))  # False
print(valid_mountain_array([0, 3, 2, 1]))  # True
print(valid_mountain_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # False
