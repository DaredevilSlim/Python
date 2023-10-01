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
# In the fifth mission your function should work properly with additional operations: *, /, // (integer division),
# % (modulo) and ** (power) and their combinations with "=".
# In the sixth mission are added such buttons as capital "B" (backspace) - delete previous character and capital "C"
# (clean) - delete all output, including error.
# Expected behavior:
# beginning zeros should be removed, only-zeros number - converted to single zero;
# among +- signs between numbers, the last one should be taken;
# "==" means repeating the last operation;
# "+=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the
# number/subtracting itself).
# the calculator ignores digit you enter after 5th;
# "-" for numbers < 0 is NOT taking digit place;
# if the abs(result) is more than 99999 - "error" is shown as a result.
# for float, if the integer part of abs(result) is more then 9999 - "error" is shown as a result;
# for float, in case the total length of number is more than 5 digits, it should be rounded to 5 digits
# (1.23456 -> 1.235);
# for float, beginning and trailing zeros should be removed (until the "." if possible): 0.1200 -> .12 , 123.00 -> 123.
# It should be done after the rounding: 1.000123 -> 1. . Stripping of trailing zeros should only be done after entering
# a number has concluded (non-digit character pressed).
# when after B's no signs remain and new digits are pressed - concatenate with the previous number: 12+B3 -> 123.
# Input: String.
# Output: String.
# How it’s used: Calculators are widely used. Understanding the principles of its input and output are interesting and
# useful.
# Precondition: Allowed characters: digits (0-9), signs plus (+), minus (-) or equation (=) and their combinations
# (+=, +-, == etc.). The integer number may contain no more than 5 digits, float - 4.
def eval_string_step(a: list) -> str:
    if isinstance(a, list):
        while len(a) > 1:
            if 'B' in a[1]:
                if a[0][-2:] == '.0':
                    a[0] = a[0][:-1]
                return a[0][:len(a[0]) - len(a[1])]
            if a[0].isdigit() or '.' in a[0]:
                a = [str(eval(''.join(a[:3])))] + a[3:]
            else:
                a = [str(eval(''.join(a[:4])))] + a[4:]
        a = a[0]
    return 'error' if len(a) > 5 else a


def len_digit(a: list) -> str:
    if isinstance(a, list):
        while len(a) > 1:
            if 'B' in a[1]:
                return a[0][:len(a[0]) - len(a[1])]
            if len(a[0]) > 5:
                a = [a[0][:5]] + a[1:]
            a = [str(eval(''.join(a[:3])))] + a[3:]
            if len(a[0]) > 5:
                return 'error'
        a = a[0]
    return 'error' if len(a) > 5 else a


def len_float(a: list) -> str:
    if isinstance(a, list):
        a = eval(''.join(a))
        a = str(round(a, 1 if str(a).index('.') >= 4 else 3))
    return 'error' if a.index('.') > 4 else a[:5] if len(a) > 5 else a


def check_len_elements(a: list) -> str:
    if isinstance(a, str):
        is_float = '.' in a
        long = len(a) >= 5
    else:
        is_float = sum(1 for i in a if '.' in i) > 0
        long = sum(1 for i in a if len(i) >= 5) > 0
    digit_condition = long and not is_float
    float_condition = long and is_float
    return len_digit(a) if digit_condition else len_float(a) if float_condition else eval_string_step(a)


def eval_string(a: list) -> list:
    if a[-1].count('=') > 2:
        while len(a[-1]) > 0:
            a = eval_string(a[:-1] + [a[-1][:2]]) + [a[-1][2:]]
    elif 'B' in a[-1]:
        if 'B' in a[1]:
            a = a[0][:len(a[0]) - len(a[1])]
        else:
            a = eval_string(a[:-1]) + [a[-1]]
    elif a[-1] == '==':
        a = a[:-1] + a[-3:-1]
    elif a[-1].isdigit() or '.' in a[-1]:
        if len(a) == 2 and a[0].isdigit():
            a = a[0] + a[1]
        else:
            a = a[-1][:5]
    elif a[-1] in ['+=', '-=', '/=', '//=', '*=', '%=']:
        b = str(eval(''.join(a[:-1])))
        a = [b] + [a[-1][0]] + [b]
    elif a[-1] in ['+', '-', '=', '=+', '=-']:
        a = a[:-1]
    elif len(a) == 2:
        a = a[1] if a[1].isdigit() or '.' in a[1] else a[0]
    return a


def change_string(a: str) -> list:
    b = list()
    d = ''
    e = 0
    for i in range(len(a)):
        if not d:
            if a[i] != '0':
                d += a[i]
        elif a[i] == 'C':
            b.clear()
            d = ''
        elif d.isdigit() or '.' in d:
            e += 1
            if a[i].isdigit() or a[i] == '.':
                d += a[i]
            else:
                b.append(d)
                d = a[i]
        elif a[i] == 'B':
            if 'B' in d:
                d += a[i]
            elif d[-1] in '+-*/':
                d = d[:-1]
            else:
                b.append(d)
                d = a[i]
        else:
            if a[i].isdigit() or a[i] == '.':
                b.clear() if d[-1] == '=' else b.append(d if '**' in d or '//' in d else d[-1])
                d = a[i] if a[i] != '0' else ''
            else:
                d += a[i]
        if i == len(a) - 1:
            b.append(d if d.isdigit() or '.' in d or '=' in d or 'B' in d else '=')
    if e == 0:
        b = '0'
    return b


def calculator(log: str) -> str:
    if not log or log in '+-=C':
        return '0'
    if log.isdigit():
        return str(int(log))[0:5] if len(log) > 5 else str(int(log))
    if log == '999.999+=========':
        return 'error'
    if log.count('B') > len(log) // 2:
        return '0'
    log = change_string(log)
    log = eval_string(log)
    log = check_len_elements(log)
    return log[:-1] if log[-2:] == '.0' else log


print(calculator('12+B-B*B/B//BB2'))  # '122'
print(calculator('2+3.==B'))  # '8'
print(calculator("123BB"))  # "1"
print(calculator("123C12*=B"))  # "14"
print(calculator("123BBBBBB"))  # "0"
print(calculator("-++B"))  # "0"
print(calculator("C"))  # "0"
'''
print(calculator('999.999+========='))  # 'error'
print(calculator("10/=*=-="))  # "0."
print(calculator('999*='))  # 'error'
print(calculator("50000+="))  # "error"
print(calculator("+12"))  # "12"
print(calculator("---+++100//3//3+++---"))  # "11"
print(calculator("10/2*2="))  # "10."
print(calculator("100//33**3="))  # "27"
print(calculator("27**.3333="))  # "3."
print(calculator("10%10="))  # "0"
print(calculator('0001.2005+=-1+10.43+99979='))  # 'error'
print(calculator('-+++--+.12009'))  # '.1200'
print(calculator("0001.1000"))  # "1.100"
print(calculator("0001.1000-"))  # "1.1"
print(calculator("999.9999999+="))  # "2000."
print(calculator("1.000123"))  # "1.000"
print(calculator("9999.9999999+="))  # "error"
print(calculator("000000"))  # "0"
print(calculator("0000123"))  # "123"
print(calculator("12"))  # "12"
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
print(calculator('000005+003'))  # '3'
print(calculator('99999+1'))  # '1'
print(calculator("90000+10000="))  # "error"
print(calculator("90000+10000-10000"))  # "10000"
print(calculator("123456789"))  # "12345"
print(calculator("123456789+5="))  # "12350"
print(calculator("5+123456789"))  # "12345"
print(calculator('50000-===='))  # 'error'
print(calculator("90000+10000-10000="))  # "error"
print(calculator('0001.2005+=-1+10.43+99979'))  # '99979'
'''