#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/57faefc42b531482d5000123
# Remove all exclamation marks from sentence except at the end.
# Examples
# "Hi!"     ---> "Hi!"
# "Hi!!!"   ---> "Hi!!!"
# "!Hi"     ---> "Hi"
# "!Hi!"    ---> "Hi!"
# "Hi! Hi!" ---> "Hi Hi!"
# "Hi"      ---> "Hi"
def remove(st: str) -> str:
    return st.replace('!', '') + '!'


print(remove('Hi!'))  # 'Hi!'
print(remove('Hi!!!'))  # 'Hi!!!'
print(remove('!Hi'))  # 'Hi'
print(remove('!Hi!'))  # 'Hi!'
print(remove('Hi! Hi!'))  # 'Hi Hi!'
print(remove('Hi'))  # Hi
