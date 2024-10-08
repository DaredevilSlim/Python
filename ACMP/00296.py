#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №296 - Лиса Алиса и кот Базилио
# (Время: 1 сек. Память: 16 Мб Сложность: 22%)
# Лиса Алиса и кот Базилио вырастили денежное дерево. И выросли на нем трехрублевые и пятирублевые золотые монеты. Лиса
# Алиса себе взяла трехрублевые монеты, а коту Базилио отдала пятирублевые монеты. Посетовав на свою скромность, она
# предложила впредь рассчитываться за покупки вместе, деньги давать без сдачи и минимальным числом монет. Известно, что
# они сделали покупку стоимостью N рублей, при этом они рассчитались без сдачи.
# Вам следует написать программу, которая определяет: сколько монет внес кот Базилио, и сколько монет внесла лиса Алиса.
# Входные данные - Во входном файле INPUT.TXT записано одно натуральное число N – стоимость покупки в рублях
# (7 < N < 1000).
# Выходные данные - В выходной OUTPUT.TXT выведите два целых числа через пробел: число монет, которые отдал кот Базилио
# и число монет, которые отдала лиса Алиса.
n = int(input())
i = 0
while n % 5 > 0:
    i += 1
    n -= 3
print(n // 5, i)
# Или
n = int(input())
i = 0
while (n - i * 3) % 5 != 0:
    i += 1
print((n - i * 3) // 5, i)
# Или
n = int(input())
a = 0
while n > 0:
    if n % 5 == 0:
        break
    a += 1
    n -= 3
print(n // 5, a)
# Или
n = int(input())
a = 0
b = 0
while n > 0:
    if n % 5 == 0:
        a = n // 5
        n = 0
    else:
        b += 1
    n -= 3
print(a, b)
