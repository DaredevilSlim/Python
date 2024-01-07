#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/57faf12b21c84b5ba30001b0
# Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata,
# you can assume that the input data is always a non empty string, no need to verify it.
# Examples
# "Hi!"     ---> "Hi!"
# "Hi!!!"   ---> "Hi!"
# "!Hi"     ---> "Hi!"
# "!Hi!"    ---> "Hi!"
# "Hi! Hi!" ---> "Hi Hi!"
# "Hi"      ---> "Hi!"
def remove(st: str) -> str:
    while st[-1] == '!':
        st = st[:-1]
    return st


print(remove('Hi!'))  # 'Hi!'
print(remove('Hi!!!'))  # 'Hi!'
print(remove('!Hi'))  # 'Hi!'
print(remove('!Hi!'))  # 'Hi!'
print(remove('Hi! Hi!'))  # 'Hi Hi!'
print(remove('Hi'))  # 'Hi!'
