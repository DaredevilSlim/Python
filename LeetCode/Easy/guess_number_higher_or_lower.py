#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.
# Example 1:
# Input: n = 10, pick = 6
# Output: 6
# Example 2:
# Input: n = 1, pick = 1
# Output: 1
# Example 3:
# Input: n = 2, pick = 1
# Output: 1
# Constraints:
# 1 <= n <= 231 - 1
# 1 <= pick <= n
def guess(num: int) -> int:
    if num > 6:
        return -1
    if num < 6:
        return 1
    return 0


def guess_number(n: int) -> int:
    minimum = 0
    maximum = n
    middle = maximum
    while guess(middle) != 0:
        if guess(middle) == 1 and minimum < middle:
            minimum = middle
        elif guess(middle) == -1 and maximum > middle:
            maximum = middle
        middle = minimum + ((maximum - minimum) // 2)
    return middle


print(guess_number(10))  # 6
'''
print(guess_number(1))  # 1
print(guess_number(1000))  # 50
print(guess_number(2))  # 1
'''
