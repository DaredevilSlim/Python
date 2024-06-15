#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/55ad04714f0b468e8200001c
# Write a function which takes a number and returns the corresponding ASCII char for that value. For ASCII table, you
# can refer to http://www.asciitable.com/
def get_char(c: int) -> str:
    return chr(c)


print(get_char(65))  # 'A'
print(get_char(33))  # '!'
print(get_char(34))  # '"'
print(get_char(35))  # '#'
print(get_char(36))  # '$'
print(get_char(37))  # '%'
print(get_char(38))  # '&'
