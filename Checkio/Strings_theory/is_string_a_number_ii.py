#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given a string. Your function should return True if the string is a valid number (contains only digits and
# "+-." at proper places), otherwise - False. Look at the mask:
# [+- ][zero or more digits][.][zero or more digits]
# Of course, not all parts are necessary (but at least one digit part is!). For example, "+10." or "-.55" are valid
# numbers, where part equal 0 is omitted.
# Input: A string (str).
# Output: Logic value (bool).
def is_number(val: str) -> bool:
    val = val.replace('.', '', 1)
    if not val:
        return False
    if val[0] in '+-':
        val = val[1:]
    return True if val.isdigit() else False


print(is_number('34'))            # True
print(is_number('df'))            # False
print(is_number(''))              # False
print(is_number('+10.0'))         # True
print(is_number('1OOO'))          # False
print(is_number('1.'))            # True
print(is_number('+.l'))           # False
print(is_number('++1+.2-'))       # False
print(is_number('3e4'))           # False
print(is_number('ITS A NUMBER'))  # False
print(is_number('1033'))          # True
print(is_number('-1000.25'))      # True
print(is_number('1l0O'))          # False
print(is_number('+1'))            # True
print(is_number('+25.25'))        # True
print(is_number('+.123'))         # True
print(is_number('-40.'))          # True
print(is_number('.1'))            # True
print(is_number('.'))             # False
print(is_number('--5'))           # False
