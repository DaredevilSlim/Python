#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вам дано положительное целое число. Определите сколько цифр оно имеет.
# Входные данные: Положительное целое число.
# Выходные данные: Целое число.
def number_length(value: int) -> int:
    return len(str(value))


print(number_length(10) )  # 2
print(number_length(0) )   # 1
print(number_length(4) )   # 1
print(number_length(44) )  # 2
