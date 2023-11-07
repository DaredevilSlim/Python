#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Calculate sum of integers from 1 to given N (including).
# Input: Integer (int).
# Output: Integer (int).
# How it’s used: this function can be used in a variety of mathematical and algorithmic contexts, such as in calculating
# the nth triangular number, determining the cost for certain operations in algorithms, etc.
# Precondition:
# 1 ≤ N ≤ 900.
def sum_upto_n(N: int) -> int:
    return sum(i for i in range(N+1))


print(sum_upto_n(1))  # 1
print(sum_upto_n(2))  # 3
print(sum_upto_n(3))  # 6
print(sum_upto_n(4))  # 10
print(sum_upto_n(5))  # 15
print(sum_upto_n(10))  # 55
print(sum_upto_n(20))  # 210
print(sum_upto_n(100))  # 5050
print(sum_upto_n(200))  # 20100
print(sum_upto_n(500))  # 125250
