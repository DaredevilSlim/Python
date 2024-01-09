#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith
# row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.
# Example 1:
# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:
# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
# Constraints:
# 1 <= n <= 231 - 1
def arrange_coins(n: int) -> int:
    a = 1
    b = 0
    c = 0
    while a + b <= n:
        b += a
        a += 1
        c += 1
    return c


print(arrange_coins(5))  # 2
print(arrange_coins(8))  # 3
print(arrange_coins(3))  # 2
