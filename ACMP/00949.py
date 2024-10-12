#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №949 - Фибоначчиева последовательность
# (Время: 1 сек. Память: 16 Мб Сложность: 17%)
# Последовательность чисел a1, a2, …, ai,… называется Фибоначчиевой, если для всех i ≥ 3 верно, что ai=ai-1+ai-2, то
# есть каждый член последовательности (начиная с третьего) равен сумме двух предыдущих.
# Ясно, что, задавая различные числа a1 и a2, мы можем получать различные такие последовательности, и любая Фибоначчиева
# последовательность однозначно задается двумя своими первыми членами.
# Будем решать обратную задачу. Вам будет дано число n и два члена последовательности: an и an+1. Вам нужно написать
# программу, которая по их значениям найдет a1 и a2.
# Входные данные - Входной файл INPUT.TXT содержит число n и значения двух членов последовательности: an и an+1
# (1 ≤ n ≤ 30, члены последовательности — целые числа, по модулю не превышающие 2×109).
# Выходные данные - В выходной файл OUTPUT.TXT выведите два числа — значения первого и второго членов этой
# последовательности.
n, a, b = map(int, input().split())
for _ in (n - 1) * ' ':
    n = b - a
    b = a
    a = n
print(a, b)
# Или
n, a, b = map(int, input().split())
c = 0
for _ in (n - 1) * ' ':
    c = b - a
    b = a
    a = c
print(a, b)
# Или
n, a, b = map(int, input().split())
c = 0
for i in range(n - 1):
    c = b - a
    b = a
    a = c
print(a, b)