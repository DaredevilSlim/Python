#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №103 - Снова A+B
# (Время: 1 сек. Память: 16 Мб Сложность: 35%)
# Требуется сложить два целых числа А и В.
# Входные данные - Во входном файле INPUT.TXT записано два неотрицательных целых числа, не превышающих 10^100, по одному
# в каждой строке.
# Выходные данные - В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел А и В,
# без лидирующих нулей.
print(eval(input() + '+' + input()))
# Или
print(int(input()) + int(input()))
