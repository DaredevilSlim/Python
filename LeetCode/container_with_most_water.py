#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
# ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of
# water (blue section) the container can contain is 49.
# Example 2:
# Input: height = [1,1]
# Output: 1
# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104
def max_area(height: list[int]) -> int:
    a = 0
    for i in range(len(height)-1):
        for j in range(len(height)-1, i, -1):
            a = max(a, (min(height[i], height[j]) * (j - i)))
    return a


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(max_area([1, 2, 4, 3]))  # 4
print(max_area([1, 1]))  # 1
print(max_area([9384, 887, 2778, 6916, 4963, 8104, 4574, 7798, 22, 293, 9308, 9431]))  # 103224
print(max_area([2, 3, 4, 5, 18, 17, 6]))  # 17
