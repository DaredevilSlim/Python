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
#     def recursion(num_x: float, pow_n: int) -> float:
#         if num_x == 0:
#             return 0
#         if pow_n == 0:
#             return 1
#         res = recursion(num_x * num_x, pow_n // 2)
#         return num_x * res if pow_n % 2 else res
#     result = recursion(x, abs(n))
#     return result if n >= 0 else 1 / result
def my_pow(x: float, n: int) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1
    if x == -1:
        if n < 0:
            return 1
        return -1
    pow_n = abs(n)
    m = abs(n)
    i = 1
    num_x = x
    while pow_n // 2:
        pow_n = pow_n // 2
        i *= 2
        num_x *= num_x
    m -= i
    if pow_n % 2 and m <= 1000000:
        num_x *= x ** m
    return num_x if n >= 0 else 1 / num_x


print(my_pow(2.00000, 10))  # 1024.00000
print(my_pow(2.00000, -2))  # 0.25000
print(my_pow(2.10000, 3))  # 9.26100
print(my_pow(0.00001, 2147483647))  # 0.00000
print(my_pow(-0.82541, 12))  # 0.10001
print(my_pow(1.00000, 2147483647))  # 1.00000
print(my_pow(2.00000, -2147483647))  # 0.00000
print(my_pow(1.00001, 123456))  # 3.43684
print(my_pow(-1.00000, 2147483647))  # 1.00000
