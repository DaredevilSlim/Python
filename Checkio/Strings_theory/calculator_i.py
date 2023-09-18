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
def len_of_string(a: list) -> str:
    while len(a) > 1:
        if len(a[0]) >= 5:
            a = [a[0][:5]] + a[1:]
        a = [str(eval(''.join(a[:3])))] + a[3:]
        if len(a[0]) > 5:
            return 'error'
    return 'error' if len(a[0]) > 5 else a[0]


def check_len_elements(a: list) -> list:
    return len_of_string(a) if sum(1 for i in a if len(i) >= 5) > 0 and ('+' in a or '-' in a) else a


def eval_string(a: list) -> list:
    if a[-1].count('=') > 2:
        while len(a[-1]) > 0:
            a = eval_string(a[:-1] + [a[-1][:2]]) + [a[-1][2:]]
    elif a[-1] == '==':
        a = a[:-1] + a[-3:-1]
    elif a[-1].isdigit():
        a = a[-1][:5]
    elif a[-1] == '+=' or a[-1] == '-=':
        b = str(eval(''.join(a[:-1])))
        a = [b] + [a[-1][0]] + [b]
    elif a[-1] in ['+', '-', '=', '=+', '=-']:
        a = a[:-1]
    elif len(a) == 2:
        a = a[1] if a[1].isdigit() else a[0]
    return a


def change_string(a: str) -> list:
    b = list()
    d = ''
    for i in range(len(a)):
        if not d:
            if a[i] != '0':
                d += a[i]
        elif d.isdigit():
            if a[i].isdigit():
                d += a[i]
            else:
                b.append(d)
                d = a[i]
        else:
            if a[i].isdigit():
                b.clear() if d[-1] == '=' else b.append(d[-1])
                d = a[i] if a[i] != '0' else ''
            else:
                d += a[i]
        if i == len(a) - 1:
            b.append(d)
    return b


def calculator(log: str) -> str:
    if not log or log in '+-=':
        return '0'
    if log.isdigit():
        return str(int(log))[0:5] if len(log) > 5 else str(int(log))
    log = change_string(log)
    log = eval_string(log)
    log = check_len_elements(log)
    return log if log == 'error' else str(eval(''.join(log)))


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
