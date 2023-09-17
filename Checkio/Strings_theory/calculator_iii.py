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
# the calculator ignores digit you enter after 5th;
# "-" for numbers < 0 is NOT taking digit place;
# if the abs(result) is more than 99999 - "error" is shown as a result.
# Input: String.
# Output: String.
# How it’s used: Calculators are widely used. Understanding the principles of its input and output are interesting and
# useful.
# Precondition: Allowed characters: digits (0-9), signs plus (+), minus (-) or equation (=) and their combinations
# (+=, +-, == etc.). The number may contain no more than 5 digits.
def len_of_string(a: list) -> str:
    while len(a) > 1:
        if len(a) >= 3:
            if len(a[0]) > 5:
                a = [a[0][:5]] + a[1:]
            c = str(eval(''.join(a[0:3])))
            if len(c) > 5:
                return 'error'
            elif len(a) > 3:
                a = [c] + [a[3:]]
            else:
                a = [c]
        else:
            return str(eval(''.join(a)))


def eval_string(a: list) -> str:
    d = 0
    for i in a:
        if len(i) >= 5:
            d += 1
    if a[-1] == '==':
        a = a[:-1] + a[-3:-1]
    elif a[-1].isdigit():
        a = a[-1]
    elif a[-1] == '+=' or a[-1] == '-=':
        b = str(eval(''.join(a[:-1])))
        a = [b] + [a[-1][0]] + [b]
    elif a[-1] in ['+', '-', '=', '=+', '=-']:
        a = a[:-1]
    elif len(a) == 2:
        a = a[1] if a[1].isdigit() else a[0]
    return len_of_string(a) if d > 0 else str(eval(''.join(a)))


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
    return log


print(calculator("90000+10000="))  # "error"
print(calculator("90000+10000-10000="))  # "error"
print(calculator("90000+10000-10000"))  # "10000"
print(calculator("123456789"))  # "12345"
print(calculator("123456789+5="))  # "12350"
print(calculator("5+123456789"))  # "12345"
print(calculator("50000+="))  # "error"
'''print(calculator("000000"))  # "0"
print(calculator("0000123"))  # "123"
print(calculator("12"))  # "12"
print(calculator("+12"))  # "12"
print(calculator(""))  # "0"
print(calculator('+'))  # '0'
print(calculator("1+2"))  # "2"
print(calculator("2+"))  # "2"
print(calculator("1+2="))  # "3"
print(calculator("1+2-"))  # "3"
print(calculator("1+2=2"))  # "2"
print(calculator("=5=10=15"))  # "15"
print(calculator("3+-2="))  # "1"
print(calculator("3+="))  # "6"
print(calculator("3+2=="))  # "7"
print(calculator("4-1=="))  # "2"
print(calculator("-=-+3-++--+-2=-"))  # "1"
print(calculator('3+2-='))  # '0'
print(calculator('+-=12='))  # '12'
print(calculator('2+3=7+7='))  # '14'
print(calculator('000005+003'))  # '3'''''
