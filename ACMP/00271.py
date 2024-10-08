#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №271 - Числа Фибоначчи - 2
# (Время: 1 сек. Память: 16 Мб Сложность: 20%)
# Числа Фибоначчи строятся следующим образом: 1, 1, 2, 3, 5, …. В этой последовательности, начиная с третьего числа,
# каждый следующий член равен сумме двух предыдущих. Получаем, что, например, шестое число равно 8, а десятое - 55.
# Требуется написать программу, которая определяет, является ли заданное число числом Фибоначчи.
# Входные данные - Входной текстовый файл INPUT.TXT содержит одно натуральное число в диапазоне от 2 до 1200000000.
# Выходные данные - Выходной файл OUTPUT.TXT должен содержать в первой строке 1, если заданное число является числом
# Фибоначчи, и 0, иначе. В первом случае во вторую строку требуется вывести его порядковый номер.
n = int(input())
a = 0
b = 1
s = 0
i = 0
while a <= n:
    if a == n:
        s = '1\n' + str(i)
    a, b = b, a + b
    i += 1
print(s)
# Или
n = int(input())
a = 0
b = 1
s = 0
for i in range(n + 2):
    if a == n:
        s = '1\n' + str(i)
    a, b = b, a + b
    if a > n:
        break
print(s)
