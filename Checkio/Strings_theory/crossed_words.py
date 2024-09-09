#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pygments.lexer import default


# In a crossword game, the player fills a rectangle with black and white squares, where each blank row and column must
# be filled with a word. The horizontal words intersect with the vertical words in common letters. In this mission only
# two words are given.
# Given a horizontal word and a vertical word, your task is to find the best crossing letter between them, defined as
# the letter that allows the rightmost crossing in the horizontal word and, in the event of a tie, the lowest crossing
# in the vertical word.
# You need to return a tuple of two integers: 1-based indexes of common letter in horizontal and vertical words
# respectively. If there is no common letter return -1, -1.
# Input: Two uppercase strings (str).
# Output: Tuple of two integers (int).
def crossed_words(hor: str, ver: str) -> tuple[int, int]:
    return max(((hor.rindex(c) + 1, ver.rindex(c) + 1) for c in set(hor) & set(ver)), default = (-1, -1))


print(crossed_words('PATO', 'PELE'))  # (1, 1)
print(crossed_words('ANJO', 'MENTORA'))  # (4, 5)
print(crossed_words('URUBU', 'POLIVALENTE'))  # (-1, -1)
print(crossed_words('ATRITO', 'TRUTA'))  # (5, 4)
