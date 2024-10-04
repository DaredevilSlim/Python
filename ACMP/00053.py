#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №53 - Раскраска таблицы умножения
# (Время: 1 сек. Память: 16 Мб Сложность: 22%)
# Таблицей умножения назовем таблицу размера n строк на m столбцов, в которой на пересечении i-ой строки и j-ого столбца
# стоит число i∙j (строки и столбцы нумеруются с единицы).
# В одной из математических школ было решено провести педагогический эксперимент. Для того, чтобы ученикам было проще
# запоминать таблицу умножения, некоторые числа в ней будут покрашены в красный, некоторые - в синий, а некоторые - в
# зеленый цвет (оставшиеся числа будут черными).
# Процесс покраски чисел можно условно разбить на четыре этапа. На первом этапе все числа красятся в черный цвет. На
# втором - все четные числа красятся в красный цвет, на третьем – все числа, делящиеся на 3, красятся в зеленый цвет, на
# четвертом - все числа, делящиеся на 5, красятся в синий цвет.
# Директор школы хочет знать, какое количество картриджей для принтеров необходимо закупить для печати таблиц. Поэтому
# ему необходима информация о том, сколько чисел какого цвета будет в одной раскрашенной таблице умножения n на m.
# Напишите программу, решающую задачу подсчета соответствующих количеств.
# Входные данные - Входной файл INPUT.TXT содержит два натуральных числа n и m (1 ≤ n,m ≤ 1000).
# Выходные данные - В первой строке выходного файла OUTPUT.TXT выведите количество чисел, покрашенных в красный цвет, во
# второй - в зеленый, в третьей - в синий, в четвертой - в черный. Следуйте формату, приведенному в примерах.
n, m = map(int, input().split())
a = 0
b = 0
c = 0
d = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        e = i * j
        if e % 5 == 0:
            c += 1
        elif e % 3 == 0:
            b += 1
        elif e % 2 == 0:
            a += 1
        else:
            d += 1
print(f'RED : {a}', f'GREEN : {b}', f'BLUE : {c}', f'BLACK : {d}', sep='\n')
# Или
n, m = map(int, input().split())
a = 0
b = 0
c = 0
d = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        e = i * j
        if e % 5 == 0:
            c += 1
        elif e % 3 == 0:
            b += 1
        elif e % 2 == 0:
            a += 1
        else:
            d += 1
print('RED : %d' % a, 'GREEN : %d' % b, 'BLUE : %d' % c, 'BLACK : %d' % d, sep='\n')
