#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/58dced7b702b805b200000be
# This series of katas will introduce you to basics of doing geometry with computers.
# Point objects have attributes x and y.
# Write a function calculating distance between Point a and Point b.
# Input coordinates fit in range −50 ⩽ x, y ⩽ 50. Tests compare expected result and actual answer with tolerance
# of 1e-6.
def distance_between_points(a: tuple, b: tuple) -> any:
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


print(distance_between_points((3, 3), (3, 3)))  # 0
print(distance_between_points((1, 6), (4, 2)))  # 5
print(distance_between_points((-10.2, 12.5), (0.3, 14.7)))  # 10.728001
