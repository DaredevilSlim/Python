#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and
# replace the last element with -1.
# After doing so, return the array.
# Example 1:
# Input: arr = [17, 18, 5, 4, 6, 1]
# Output: [18, 6, 6, 6, 1, -1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
# Example 2:
# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.
# Constraints:
# 1 <= arr.length <= 104
# 1 <= arr[i] <= 105
def replace_elements(arr: list[int]) -> list[int]:
    new_arr = []
    i = 0
    if not arr[i + 1:]:
        return [-1]
    max_arr = max(arr[i + 1:])
    while i < len(arr) - 1:
        if arr[i] == max_arr:
            max_arr = max(arr[i + 1:])
        new_arr.append(max_arr)
        i += 1
    return new_arr + [-1]


print(replace_elements([17, 18, 5, 4, 6, 1]))  # [18, 6, 6, 6, 1, -1]
print(replace_elements([400]))  # [-1]
