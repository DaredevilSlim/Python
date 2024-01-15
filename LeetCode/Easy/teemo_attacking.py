#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a
# exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time
# interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and
# the poison effect will end duration seconds after the new attack.
# You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second
# timeSeries[i], and an integer duration.
# Return the total number of seconds that Ashe is poisoned.
# Example 1:
# Input: timeSeries = [1,4], duration = 2
# Output: 4
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
# Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
# Example 2:
# Input: timeSeries = [1,2], duration = 2
# Output: 3
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
# Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
# Constraints:
# 1 <= timeSeries.length <= 104
# 0 <= timeSeries[i], duration <= 107
# timeSeries is sorted in non-decreasing order.
def find_poisoned_duration(time_series: list[int], duration: int) -> int:
    list_attack = 0
    a = -1 if time_series[0] == 0 else 0
    for i in time_series:
        if a >= i:
            list_attack += i - 1 - a
        list_attack += duration
        a = i + duration - 1
    return list_attack


print(find_poisoned_duration([1, 4], 2))  # 4
print(find_poisoned_duration([1, 2], 2))  # 3
print(find_poisoned_duration([1, 2, 3, 4, 5, 6, 7, 8, 9], 0))  # 0
print(find_poisoned_duration([1, 2, 3, 4, 5, 6, 7, 8, 9], 100000))  # 100008
print(find_poisoned_duration([1, 3, 5, 7, 9, 11, 13, 15], 3))  # 17
print(find_poisoned_duration([1, 3, 5, 7, 9, 11, 13, 15], 4))  # 18
