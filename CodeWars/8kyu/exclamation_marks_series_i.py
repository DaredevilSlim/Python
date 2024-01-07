#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/57fae964d80daa229d000126
# Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always
# a string, no need to verify it.
# Examples
# "Hi!"     ---> "Hi"
# "Hi!!!"   ---> "Hi!!"
# "!Hi"     ---> "!Hi"
# "!Hi!"    ---> "!Hi"
# "Hi! Hi!" ---> "Hi! Hi"
# "Hi"      ---> "Hi"
def remove(s: str) -> str:
    return s[:-1] if s and s[-1] == '!' else s


print(remove('Hi!'))  # 'Hi'
print(remove('Hi!!!'))  # 'Hi!!'
print(remove('!Hi'))  # '!Hi'
print(remove('!Hi!'))  # '!Hi'
print(remove('Hi! Hi!'))  # 'Hi! Hi'
print(remove('Hi'))  # 'Hi'
