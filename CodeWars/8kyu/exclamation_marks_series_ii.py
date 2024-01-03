#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/57faece99610ced690000165
# Remove all exclamation marks from the end of sentence.
# Examples
# "Hi!"     ---> "Hi"
# "Hi!!!"   ---> "Hi"
# "!Hi"     ---> "!Hi"
# "!Hi!"    ---> "!Hi"
# "Hi! Hi!" ---> "Hi! Hi"
# "Hi"      ---> "Hi"
def remove(st: str) -> str:
    while st[-1] == '!':
        st = st[:-1]
    return st


print(remove('Hi!'))  # Hi
print(remove('Hi!!!'))  # Hi
print(remove('!Hi'))  # !Hi
print(remove('!Hi!'))  # !Hi
print(remove('Hi! Hi!'))  # Hi! Hi
print(remove('Hi'))  # Hi
