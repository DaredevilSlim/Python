#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
# one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and
# loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:
# Input: nums = [1,1]
# Output: [1,2]
def find_error_nums(nums: list[int]) -> list[int]:
    a = [i for i in range(1, len(nums) + 1)]
    b = list(set(a).difference(nums))
    nums = sorted(nums + b)
    i = 0
    while i < len(a) and a[i] == nums[i]:
        i += 1
    return [a[i - 1]] + b


print(find_error_nums([1, 5, 3, 2, 2, 7, 6, 4, 8, 9]))  # [2, 10]
print(find_error_nums([1, 2, 2, 4]))  # [2, 3]
print(find_error_nums([1, 1]))  # [1, 2]
print(find_error_nums([2, 2]))  # [2, 1]
print(find_error_nums([3, 2, 3, 4, 6, 5]))  # [3, 1]
