#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №1112 - Сумма цифр числа
# (Время: 1 сек. Память: 16 Мб Сложность: 7%)
# Найдите сумму цифр трехзначного натурального числа.
# Входные данные - Входной файл INPUT.TXT содержит трехзначное натуральное число.
# Выходные данные - В выходной файл OUTPUT.TXT выведите сумму цифр заданного числа.
print(sum(int(i) for i in input()))