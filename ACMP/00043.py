#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №43 - Нули
# (Время: 1 сек. Память: 16 Мб Сложность: 16%)
# Требуется найти самую длинную непрерывную цепочку нулей в последовательности нулей и единиц.
# Входные данные - В единственной строке входного файла INPUT.TXT записана последовательность нулей и единиц (без
# пробелов). Суммарное количество цифр от 1 до 100.
# Выходные данные - В единственную строку выходного файла OUTPUT.TXT нужно вывести искомую длину цепочки нулей.
a = 0
b = 0
r = 0
for i in input():
    if i == '0':
        b = 0
        a += 1
        if a > r:
            r = a
    else:
        a = 0
        b += 0
        if b > r:
            r = b
print(r)
