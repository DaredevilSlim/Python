#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given two integer arrays startTime and endTime and given an integer queryTime.
# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
# Return the number of students doing their homework at time queryTime. More formally, return the number of students
# where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
# Example 1:
# Input: startTime = [1, 2, 3], endTime = [3, 2, 7], queryTime = 4
# Output: 1
# Explanation: We have 3 students where:
# The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
# The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
# The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at
# time 4.
# Example 2:
# Input: startTime = [4], endTime = [4], queryTime = 4
# Output: 1
# Explanation: The only student was doing their homework at the queryTime.
# Constraints:
# startTime.length == endTime.length
# 1 <= startTime.length <= 100
# 1 <= startTime[i] <= endTime[i] <= 1000
# 1 <= queryTime <= 1000
def busy_student(start_time: list[int], end_time: list[int], query_time: int) -> int:
    count = 0
    for start, end in zip(start_time, end_time):
        if start <= query_time <= end:
            count += 1
    return count


print(busy_student([1, 2, 3], [3, 2, 7], 4))  # 1
print(busy_student([4], [4], 4))  # 1
