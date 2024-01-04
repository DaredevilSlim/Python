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
    if num > 50:
        return -1
    if num < 50:
        return 1
    return 0


def guess_number(n: int) -> int:
    a = n
    co = 0
    while co <= 7 and guess(n) != 0:
        print(f'begin n - {n}')
        if guess(n) == 1:
            n = round(n / 2)
            print(f'equal to 1, n - {n}, a - {a}')
        elif guess(n) == -1:
            a = round(n / 2)
            n = round(n - a / 2) if a > 1 else a
            print(f'equal to -1, n - {n}, a - {a}')
        co += 1
    return n


print(guess_number(1000))
