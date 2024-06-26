#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given two positive integers a and b, return the number of common factors of a and b.
# An integer x is a common factor of a and b if x divides both a and b.
# Example 1:
# Input: a = 12, b = 6
# Output: 4
# Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
# Example 2:
# Input: a = 25, b = 30
# Output: 2
# Explanation: The common factors of 25 and 30 are 1, 5.
# Constraints:
# 1 <= a, b <= 1000
def common_factors(a: int, b: int) -> int:
    def factors(n: int) -> list:
        result = []
        for i in range(1, n + 1):
            if n % i == 0:
                result.append(i)
        return result
    return len(set(factors(a)).intersection(factors(b)))


print(common_factors(12, 6))  # 4
print(common_factors(25, 30))  # 2
