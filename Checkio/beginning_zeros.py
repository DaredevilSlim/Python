#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вам дана строка состоящая только из цифр. Вам нужно посчитать сколько нулей ("0") находится в начале строки.
# Входные данные: Строка, состоящая только из цифр.
# Выходные данные: Целое число.
# Строка может иметь цифры: 0-9

def beginning_zeros(a: str) -> int:
    return len(a) - len(a.lstrip('0'))


print(beginning_zeros("100"))          # 0
print(beginning_zeros("001"))          # 2
print(beginning_zeros("100100"))       # 0
print(beginning_zeros("001001"))       # 2
print(beginning_zeros("012345679"))    # 1
print(beginning_zeros("0000"))         # 4
