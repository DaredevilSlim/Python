#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given two integers, n and k, the task is to count how many numbers between 1 and n (inclusive) are divisible by k.
# Input: Two integers (int).
# Output: Integer (int).
# How it’s used: this function can be useful in number theory problems, statistical computations, and various other
# mathematical and practical scenarios where such a count is needed.
# Precondition:
# 1 <= k <= n <= 109.
def count_divisible(n: int, k: int) -> int:
    return n // k


print(count_divisible(10, 2))  # 5
print(count_divisible(10, 3))  # 3
print(count_divisible(10, 5))  # 2
print(count_divisible(15, 4))  # 3
print(count_divisible(20, 6))  # 3
print(count_divisible(100, 10))  # 10
print(count_divisible(200, 25))  # 8
print(count_divisible(50, 7))  # 7
print(count_divisible(60, 8))  # 7
print(count_divisible(70, 9))  # 7
