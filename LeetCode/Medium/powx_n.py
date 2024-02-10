#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Constraints:
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104
def my_pow(x: float, n: int) -> float:
    if n == 0 or abs(x) == 1.0:
        if x < 0:
            if n < 0:
                return 1
            return -1
        return 1
    if abs(n) > 1000000:
        return 0
    pow_x = x
    i = 1
    while i < abs(n):
        if 0 < pow_x < 0.000001:
            return 0
        pow_x *= x
        i += 1
    return pow_x if n > 0 else 1 / pow_x


print(my_pow(2.00000, 10))  # 1024.00000
print(my_pow(2.10000, 3))  # 9.26100
print(my_pow(2.00000, -2))  # 0.25000
print(my_pow(0.00001, 2147483647))  # 0.00000
print(my_pow(-0.82541, 12))  # 0.10001
print(my_pow(1.00000, 2147483647))  # 1.00000
print(my_pow(2.00000, -2147483647))  # 1.00000
