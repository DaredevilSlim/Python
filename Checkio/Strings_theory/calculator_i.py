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
# In the first mission only digits and single signs (only +, -, =) between them are used.
# Expected behavior:
# beginning zeros should be removed, only-zeros number - converted to single zero.
# Input: String.
# Output: String.
# How it’s used: Calculators are widely used. Understanding the principles of its input and output are interesting and
# useful.
# Precondition: Allowed characters: digits (0-9), single signs plus (+), minus (-) or equation (=) between digit blocks.
# NO combinations of signs (+=, +- etc.).
def calculator(log: str) -> str:
    if not log or log in '+-=':
        return '0'
    if log.isdigit():
        return str(int(log))
    for i in '+-=':
        log = log.replace(i, ' ' + i + ' ')
    log = ''.join(str(int(i)) if i not in '+-=' else i for i in log.split())
    if log[-1] in '+=-':
        return str(eval(log[:-1]))
    for i in '=+-':
        if i in log:
            return log.split(i)[-1]


print(calculator('000000'))  # "0"
print(calculator('0000123'))  # "123"
print(calculator('12'))  # "12"
print(calculator('+12'))  # "12"
print(calculator(''))  # "0"
print(calculator('1+2'))  # "2"
print(calculator('2+'))  # "2"
print(calculator('1+2='))  # "3"
print(calculator('1+2-'))  # "3"
print(calculator('1+2=2'))  # "2"
print(calculator('=5=10=15'))  # "15"
print(calculator('000005+003'))  # '3'
print(calculator('000005+003='))  # '8'
print(calculator('+'))  # '0'
