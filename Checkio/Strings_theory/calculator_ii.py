#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# The first solid-state electronic calculator was created in the early 1960s. Pocket-sized devices became available in
# the 1970s, especially after the Intel 4004, the first microprocessor, was developed by Intel for the Japanese
# calculator company Busicom. They later became used commonly within the petroleum industry (oil and gas). Find more on
# wikipedia page...
# In this series of missions you are going to build an elementary calculator.
# As an input, you get a sequence of keys pressed, and, as the result of that function, you should show what will be
# shown on the screen when the last key is pressed. Be attentive, it's not always the result of the expression.
# Actually, playing with the physical calculator or app will really help you to catch edge cases.
# In this mission the combinations of signs are presented.
# Expected behavior:
# beginning zeros should be removed, only-zeros number - converted to single zero;
# among +- signs between numbers, the last one should be taken;
# "==" means repeating the last operation;
# "+=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the
# number/subtracting itself).
# Input: String.
# Output: String.
def calculator(log: str) -> str:
    if not log or log in '+-=':
        return '0'
    if log.isdigit():
        return str(int(log))
    return ''


print(calculator("3+="))  # "6"
print(calculator("3+2=="))  # "7"
print(calculator("4-1=="))  # "2"
print(calculator("3+-2="))  # "1"
print(calculator("-=-+3-++--+-2=-"))  # "1"
print(calculator("000000"))  # "0"
print(calculator("0000123"))  # "123"
print(calculator("12"))  # "12"
print(calculator("+12"))  # "12"
print(calculator(""))  # "0"
print(calculator("1+2"))  # "2"
print(calculator("2+"))  # "2"
print(calculator("1+2="))  # "3"
print(calculator("1+2-"))  # "3"
print(calculator("1+2=2"))  # "2"
print(calculator("=5=10=15"))  # "15"
