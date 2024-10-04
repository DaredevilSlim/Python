#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №63 - Загадка
# (Время: 1 сек. Память: 16 Мб Сложность: 18%)
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Входные данные - Входной файл INPUT.TXT содержит два натуральных числа S и P, разделенных пробелом.
# Выходные данные - В выходной файл OUTPUT.TXT выведите два числа Х и Y, загаданные Петей. Числа следует вывести в
# порядке неубывания своих значений, разделенные пробелом.
s, p = map(int, input().split())
i = 1
while s > i:
    if (s - i) * i == p:
        print(i, s - i)
        i = s
    i += 1
# Или
s, p = map(int, input().split())
for i in range(s):
    if (s - i) * i == p:
        print(i, s - i)
        break
# Или
s, p = map(int, input().split())
for i in range((s // 2) + 1):
    if (s - i) * i == p:
        print(i, s - i)
# Или
s, p = map(int, input().split())
for i in range(s):
    a = s - i
    b = s - a
    if a * b == p:
        print(b, a)
        break
# Или
s, p = map(int, input().split())
i = 1
a = 0
b = 0
while s > i:
    a = s - i
    b = s - a
    if a * b == p:
        i = s
    i += 1
print(b, a)
