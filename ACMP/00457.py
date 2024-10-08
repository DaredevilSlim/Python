#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №457 - Постоянная Капрекара
# Возьмем четырехзначное число, в котором не все цифры одинаковы, например 6264. Расположим цифры сначала в порядке
# убывания - 6642; затем, переставив их в обратном порядке, получим 2466. Вычтем последнее число из 6642. На следующем
# шаге с полученной разностью проделаем тоже самое. Через несколько таких действий получится число, переходящее само в
# себя и называемое постоянной Капрекара. Требуется написать программу, которая находит эту постоянную и количество
# шагов для ее получения из заданного четырехзначного числа.
# Входные данные - Входной файл INPUT.TXT содержит одну строку, в которой записано четырехзначное число.
# Выходные данные - В выходной файл OUTPUT.TXT записываются: в первой строке постоянная Капрекара, во второй –
# количество шагов для ее получения.
a = input()
b = 0
c = 0
while a != b:
    d = ''.join(sorted(a))
    b = str(abs(int(d[::-1]) - int(f'{d:0<4}')))
    if a != b:
        a = b
        b = 0
        c += 1
print(a, c, sep='\n')
# Или
a = input()
b = 0
c = 0
while a != b:
    d = ''.join(sorted(a))
    b = str(abs(int(d[::-1]) - int('{0:0<4}'.format(d))))
    if a != b:
        a = b
        b = 0
        c += 1
print(a, c, sep='\n')
# Или
a = input()
b = a
c = 0
d = 0
while b != d:
    d = str(abs(int(''.join(sorted(b, reverse=True))) - int('{0:0<4}'.format(''.join(sorted(b))))))
    if b != d:
        b = d
        d = 0
        c += 1
print(d, c, sep='\n')


# Или
def g(s):
    return ''.join(sorted(s, reverse=True))


def h(s):
    return ''.join(sorted(s))


a = input()
b = a
c = 0
d = 0
while b != d:
    d = str(abs(int(g(b)) - int('{0:0<4}'.format(h(b)))))
    if b != d:
        b = d
        d = 0
        c += 1
print(d, c, sep='\n')
