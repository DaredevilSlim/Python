#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for
# all 0 < i < nums.length.
# Return the number of steps performed until nums becomes a non-decreasing array.
# Example 1:
# Input: nums = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]
# Output: 3
# Explanation: The following are the steps performed:
# - Step 1: [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11] becomes [5, 4, 4, 7, 6, 11, 11]
# - Step 2: [5, 4, 4, 7, 6, 11, 11] becomes [5, 4, 7, 11, 11]
# - Step 3: [5, 4, 7, 11, 11] becomes [5, 7, 11, 11]
# [5, 7, 11, 11] is a non-decreasing array. Therefore, we return 3.
# Example 2:
# Input: nums = [4, 5, 7, 7, 13]
# Output: 0
# Explanation: nums is already a non-decreasing array. Therefore, we return 0.
# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
def total_steps(nums: list[int]) -> int:
    '''
    start = len(nums)
    count = 0
    while start > 0:
        start = 0
        i = 1
        temp = []
        while i < len(nums):
            if nums[i - 1] > nums[i]:
                temp.append(i)
                start += 1
            i += 1
        j = 0
        temp = temp[::-1]
        while j < len(temp):
            nums.pop(temp[j])
            j += 1
        if start > 0:
            count += 1
    return count
    '''
    start = len(nums)
    count = 0
    while start > 0:
        start = 0
        i = 1
        temp = []
        print(f'step before {nums}')
        while i < len(nums):
            print(f'temp before {temp}')
            if nums[i - 1] > nums[i]:
                print(f'outside if {nums[i - 1]} > {nums[i]} = {nums[i - 1] > nums[i]}')
                j = i - 1
                i += 1
                while i < len(nums) and nums[i - 1] > nums[i]:
                    print(f'inside {nums[i - 1]} > {nums[i]} = {nums[i - 1] > nums[i]}')
                    i += 1
                temp.append(nums[j])
                start += 1
                print(f'if temp after {temp}')
            else:
                print(f'outside else {nums[i - 1]} > {nums[i]} = {nums[i - 1] > nums[i]}')
                temp.append(nums[i])
                i += 1
                print(f'else temp after {temp}')
            print(f'temp after {temp}')

        if start > 0:
            count += 1
        nums = temp if temp != [] else nums
        print(f'step after {nums}')
    return count
            
            
print(total_steps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]))  # 3
print(total_steps([4, 5, 7, 7, 13]))  # 0
print(total_steps([10, 6, 5, 10, 15]))  # 1
print(total_steps([10, 1, 2, 3, 4, 5, 6, 1, 2, 3]))  # 1
