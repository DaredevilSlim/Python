#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/643af0fa9fa6c406b47c5399
# Given a point in a Euclidean plane (x and y), return the quadrant the point exists in: 1, 2, 3 or 4 (integer). x and y
# are non-zero integers, therefore the given point never lies on the axes.
# There are four quadrants:
# First quadrant, the quadrant in the top-right, contains all points with positive X and Y
# Second quadrant, the quadrant in the top-left, contains all points with negative X, but positive Y
# Third quadrant, the quadrant in the bottom-left, contains all points with negative X and Y
# Fourth quadrant, the quadrant in the bottom-right, contains all points with positive X, but negative Y
def quadrant(x: int, y: int) -> int:
    return 3 if x < 0 > y else 2 if x < 0 < y else 4 if x > 0 > y else 1


print(quadrant(1, 2))  # 1
print(quadrant(1, 1))  # 1
print(quadrant(3, 5))  # 1
print(quadrant(-10, 100))  # 2
print(quadrant(-1, -9))  # 3
print(quadrant(19, -56))  # 4
print(quadrant(-60, -12))  # 3
