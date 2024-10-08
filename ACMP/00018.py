#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №18 - Факториал
# (Время: 1 сек. Память: 16 Мб Сложность: 42%)
# Требуется вычислить факториал целого числа N. Факториал обозначают как N! и вычисляют по формуле:
# N! = 1 * 2 * 3 * … * (N-1) * N, причем 0! = 1.
# Так же допустимо рекуррентное соотношение: N! = (N-1)! * N
# Входные данные - В единственной строке входного файла INPUT.TXT записано одно целое неотрицательное число N
# (N < 1000).
# Выходные данные - В выходной файл OUTPUT.TXT нужно вывести одно целое число — значение N!.
a = 1
for i in range(1, int(input()) + 1):
    a *= i
print(a)

