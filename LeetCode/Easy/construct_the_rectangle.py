#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your
# job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
# The area of the rectangular web page you designed must equal to the given target area.
# The width W should not be larger than the length L, which means L >= W.
# The difference between length L and width W should be as small as possible.
# Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.
# Example 1:
# Input: area = 4
# Output: [2,2]
# Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].
# But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2].
# So the length L is 2, and the width W is 2.
# Example 2:
# Input: area = 37
# Output: [37,1]
# Example 3:
# Input: area = 122122
# Output: [427,286]
# Constraints:
# 1 <= area <= 107
def construct_rectangle(area: int) -> list[int]:
    list_area = list()
    a = 1
    while area // a >= a <= (area // 2) + 1:
        if area % a == 0:
            list_area = [area // a, a]
        a += 1
    return list_area


print(construct_rectangle(4))  # [2, 2]
print(construct_rectangle(37))  # [37, 1]
print(construct_rectangle(122122))  # [427, 286]
