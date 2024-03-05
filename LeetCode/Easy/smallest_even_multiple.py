#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
# Example 1:
# Input: n = 5
# Output: 10
# Explanation: The smallest multiple of both 5 and 2 is 10.
# Example 2:
# Input: n = 6
# Output: 6
# Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.
# Constraints:
# 1 <= n <= 150
def smallest_even_multiple(n: int) -> int:
    one = []
    for i in range(1, n + 1):
        one.append(i * n)
        if i * 2 in one:
            return i * 2
    return 2


print(smallest_even_multiple(5))  # 10
print(smallest_even_multiple(6))  # 6
