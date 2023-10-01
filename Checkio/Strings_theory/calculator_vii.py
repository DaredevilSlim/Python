#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The HP 12c financial calculator is still produced. It was introduced in 1981 and is still being made with few changes.
# The HP 12c featured the reverse Polish notation mode of data entry. In 2003 several new models were released,
# including an improved version of the HP 12c, the "HP 12c platinum edition" which added more memory, more built-in
# functions, and the addition of the algebraic mode of data entry. Find more on wikipedia page...
# In this series of missions you are going to build an elementary calculator.
# As an input, you get a sequence of keys pressed, and, as the result of that function, you should show what will be
# shown on the screen when the last key is pressed. Be attentive, it's not always the result of the expression.
# Actually, playing with the physical calculator or app will really helps you to catch edge cases.
# In the seventh mission the memory should be implemented with such operations: capital "A" (add, +), capital "S"
# (subtract, -), capital "G" (get value) and capital "E" (erase memory).
# Expected behavior:
# beginning zeros should be removed, only-zeros number - converted to single zero;
# among +- signs between numbers, the last one should be taken;
# "==" means repeating the last operation;
# "+=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the
# number/subtracting itself);
# the calculator ignores digit you enter after 5th;
# "-" for numbers < 0 is NOT taking digit place;
# if the abs(result) is more than 99999 - "error" is shown as a result;
# for float, if the integer part of abs(result) is more then 9999 - "error" is shown as a result;
# for float, in case the total length of number is more than 5 digits, it should be rounded to 5 digits
# (1.23456 -> 1.235);
# for float, beginning and trailing zeros should be removed (until the "." if possible): 0.1200 -> .12 ,
# 123.00 -> 123. . It should be done after the rounding: 1.000123 -> 1. . Stripping of trailing zeros should only be
# done after entering a number has concluded (non-digit character pressed);
# when after B's no signs remain and new digits are pressed - concatenate with the previous number: 12+B3 -> 123 ;
# "A"/"S" increase/decrease memory by previous number with cleaning the output;
# "G" insert memory value if used after operation, clean output and insert value otherwise.
# Input: String.
# Output: String.
# How it’s used: Calculators are widely used. Understanding the principles of its input and output are interesting and
# useful.
# Precondition: Allowed characters: digits (0-9), dot (.), signs +, -, =, *, /, //, %, ** and their combinations (+=,
# +-, ==, %= etc.), letters "B", "C", "A", "S", "G", "E". The integer number may contain no more than 5 digits,
# float - 4.
def len_of_string(a: list) -> str:
    while len(a) > 1:
        if len(a[0]) >= 5:
            a = [a[0][:5]] + a[1:]
        a = [str(eval(''.join(a[:3])))] + a[3:]
        if len(a[0]) > 5:
            return 'error'
    return 'error' if len(a[0]) > 5 else a[0]


def check_len_elements(a: list) -> str:
    condition = sum(1 for i in a if len(i) >= 5) > 0 and ('+' in a or '-' in a)
    return len_of_string(a) if condition else str(eval(''.join(a)))


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
    return log



print(calculator(""))  # "0"
print(calculator("000000"))  # "0"
print(calculator("0000123"))  # "123"
print(calculator("12"))  # "12"
print(calculator("100A90S"))  # "0"
print(calculator("100A90SG"))  # "10"
print(calculator("100A90EG"))  # "0"
print(calculator("ASG"))  # "0"
print(calculator("123BB"))  # "1"
print(calculator("123C12*=B"))  # "14"
print(calculator("123BBBBBB"))  # "0"
print(calculator("C"))  # "0"
print(calculator("-++B"))  # "0"
print(calculator("10/2*2="))  # "10."
print(calculator("10/=*=-="))  # "0."
print(calculator("100//33**3="))  # "27"
print(calculator("10%10="))  # "0"
print(calculator("---+++100//3//3+++---"))  # "11"
print(calculator("27**.3333="))  # "3."
print(calculator("0001.1000"))  # "1.100"
print(calculator("0001.1000-"))  # "1.1"
print(calculator("999.9999999+="))  # "2000."
print(calculator("1.000123"))  # "1.000"
print(calculator("9999.9999999+="))  # "error"
print(calculator("90000+10000="))  # "error"
print(calculator("90000+10000-10000="))  # "error"
print(calculator("90000+10000-10000"))  # "10000"
print(calculator("123456789"))  # "12345"
print(calculator("123456789+5="))  # "12350"
print(calculator("5+123456789"))  # "12345"
print(calculator("50000+="))  # "error"
print(calculator("3+="))  # "6"
print(calculator("3+2=="))  # "7"
print(calculator("4-1=="))  # "2"
print(calculator("3+-2="))  # "1"
print(calculator("-=-+3-++--+-2=-"))  # "1"
print(calculator("+12"))  # "12"
print(calculator("1+2"))  # "2"
print(calculator("2+"))  # "2"
print(calculator("1+2="))  # "3"
print(calculator("1+2-"))  # "3"
print(calculator("1+2=2"))  # "2"
print(calculator("=5=10=15"))  # "15"
