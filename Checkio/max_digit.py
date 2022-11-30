#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# У вас есть число и нужно определить какая цифра из этого числа является наибольшей.
# Входные данные: Положительное целое число.
# Выходные данные: Целое число (0-9).

def max_digit(value: int) -> int:
    return max(map(int, str(value)))


print(max_digit(10))     # 1
print(max_digit(0))      # 0
print(max_digit(52))     # 5
print(max_digit(634))    # 6
print(max_digit(1))      # 1
print(max_digit(10000))  # 1
