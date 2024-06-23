#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given an integer array nums and an integer k.
# In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is
# an integer from the range [-k, k]. You can apply this operation at most once for each index i.
# The score of nums is the difference between the maximum and minimum elements in nums.
# Return the minimum score of nums after applying the mentioned operation at most once for each index in it.
# Example 1:
# Input: nums = [1], k = 0
# Output: 0
# Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
# Example 2:
# Input: nums = [0, 10], k = 2
# Output: 6
# Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.
# Example 3:
# Input: nums = [1, 3, 6], k = 3
# Output: 0
# Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.
# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 104
# 0 <= k <= 104
def smallest_range_i(nums: list[int], k: int) -> int:
    max_num = max(nums)
    min_num = min(nums)
    temp = max_num - min_num
    for i in range(k, -1, -1):
        for j in range(k, -1, -1):
            val = (max_num - i) - (min_num + j)
            if val <= 0:
                return 0
            elif val <= temp:
                return val


print(smallest_range_i([1], 0))  # 0
print(smallest_range_i([0, 10], 2))  # 6
print(smallest_range_i([1, 3, 6], 3))  # 0
print(smallest_range_i([506, 4763, 8681, 4243, 4040, 8587, 9235, 442, 1865, 2820], 5899))  # 0
