#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №446 - Табло
# (Время: 1 сек. Память: 16 Мб Сложность: 20%)
# На хоккейном стадионе в одном большом городе расположено большое прямоугольное табло. Оно имеет n строк и m столбцов
# (то есть состоит из n x m ячеек). Во время хоккейного матча это табло служит для отображения счета и времени,
# прошедшего с начала тайма, а в перерывах на нем показывают различную рекламу.
# В связи с этим возникла задача проверки возможности показа на этом табло определенной рекламной заставки. Заставка
# также, как и табло, имеет размер n строк на m столбцов. Каждая из ячеек заставки окрашена в один из четырех цветов -
# трех основных: красный - R, зеленый - G, синий - B и черный - .(точка).
# Каждая из ячеек табло характеризуется своими цветопередаточными возможностями. Любая из ячеек табло может отображать
# черный цвет - это соответствует тому, что на нее вообще не подается напряжение. Также каждая из ячеек может отображать
# некоторое подмножество множества основных цветов. В этой задаче эти подмножества будут кодироваться следующим образом:
# 0 - ячейка может отображать только черный цвет;
# 1 - ячейка может отображать только черный и синий цвета;
# 2 - ячейка может отображать только черный и зеленый цвета;
# 3 - ячейка может отображать только черный, зеленый и синий цвета;
# 4 - ячейка может отображать только черный и красный цвета;
# 5 - ячейка может отображать только черный, красный и синий цвета;
# 6 - ячейка может отображать только черный, красный и зеленый цвета;
# 7 - ячейка может отображать только черный, красный, зеленый и синий цвета.
# Напишите программу, которая по описанию табло и заставки определяет: возможно ли на табло отобразить эту заставку.
# Входные данные - Первая строка входного файла INPUT.TXT содержит целые числа n и m (1 ≤ n, m ≤ 100). Далее идут n
# строк по m символов каждая - описание заставки. Каждый из символов описания заставки принадлежит множеству {R, G, B,
# .} . Их значения описаны выше.
# После этого идет описание табло. Оно содержит n строк по m чисел, разделенных пробелами. Значения чисел описаны выше.
# Выходные данные - В выходной файл OUTPUT.TXT выведите YES, если на табло возможно отобразить заставку и NO - в
# противном случае.
n, m = map(int, input().split())
a = ''
for i in range(n * 2):
    a += input().replace(' ', '')
c = {'R': '4567', 'G': '2367', 'B': '1357', '.': '01234567'}
b = len(a) // 2
e = 0
for d in range(b):
    if a[d + n * m] in c[a[d]]:
        e += 1
print('YES' if e == b else 'NO')
# Или
n, m = map(int, input().split())
a, b, e = '', '', ''
for i in range(n):
    a += input()
for j in range(n):
    b += input().replace(' ', '')
c = {'R': '4567', 'G': '2367', 'B': '1357', '.': '01234567'}
for d in range(len(b)):
    if b[d] in c[a[d]]:
        e += '1'
print('YES' if len(e) == len(a) else 'NO')
# Или
n, m = map(int, input().split())
a, b, e = '', '', ''
a += ''.join([input() for i in range(n)])
b += ''.join([input().replace(' ', '') for j in range(n)])
c = {'R': '4567', 'G': '2367', 'B': '1357', '.': '01234567'}
e += ''.join(['1' for d in range(len(b)) if b[d] in c[a[d]]])
print('YES' if len(e) == len(a) else 'NO')
# Или
n, m = map(int, input().split())
a, b, e = '', '', ''
for i in range(n):
    for j in input():
        a += j
for k in range(n):
    for l in input().split():
        b += l
c = {'R': '4567', 'G': '2367', 'B': '1357', '.': '01234567'}
for d in range(len(b)):
    if b[d] in c[a[d]]:
        e += '1'
print('YES' if len(e) == len(a) else 'NO')
# Или
n, m = map(int, input().split())
a, b, e = [], [], []
for i in range(n):
    for j in input():
        a.append(j)
for k in range(n):
    for l in input().split():
        b.append(int(l))
c = {'R': [4, 5, 6, 7], 'G': [2, 3, 6, 7], 'B': [1, 3, 5, 7], '.': [0, 1, 2, 3, 4, 5, 6, 7]}
for d in range(len(b)):
    if b[d] in c[a[d]]:
        e.append(1)
print('YES' if sum(e) == len(a) else 'NO')
