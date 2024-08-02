#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Champernowne word 1234567891011121314151617181920212223…, also known as the counting series, is an infinitely long
# string of digits made up of all positive integers written out in ascending order without any separators. This function
# should return the digit at position n of the Champernowne word. Position counting again starts from zero.
# Input: Integer (int).
# Output: Integer (int).
# The mission was taken from Python CCPS 109. It is taught for Ryerson Chang School of Continuing Education by Ilkka
# Kokkarinen
def counting_series(n: int) -> int:
    len_n = 0
    i = 1
    new = str(i)
    while len_n < n:
        i += 1
        new += str(i)
        len_n += len(str(i))
    return int(new[n])


print(counting_series(0))  # 1
print(counting_series(10))  # 0
print(counting_series(100))  # 5

