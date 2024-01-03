#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/56b1f01c247c01db92000076
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
def double_char(s: str) -> str:
    new_s = ''
    for i in s:
        new_s += i * 2
    return new_s


print(double_char('String'))  # 'SSttrriinngg'
print(double_char('Hello World'))  # 'HHeelllloo  WWoorrlldd'
print(double_char('1234!_ '))  # '11223344!!__  '
