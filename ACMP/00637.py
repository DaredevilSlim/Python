#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №637 - NEERC
# В полуфинале студенческого чемпионата мира по программированию NEERC (http://neerc.ifmo.ru) участвуют команды из n
# институтов. Участники для проведения соревнований распределяются по k залам, каждый из которых имеет размеры,
# достаточные для размещения всех команд от всех институтов. При этом по правилам соревнований в одном зале может
# находиться не более одной команды от института.
# Многие институты уже подали заявки на участие в полуфинале. Оргкомитет полуфинала хочет допустить до участия
# максимально возможное количество команд. При этом, разумеется, должна существовать возможность рассадить их по залам
# без нарушения правил.
# Напишите программу, определяющую максимальное количество команд, которые можно допустить до участия в полуфинале.
# Входные данные - Первая строка входного файла INPUT.TXT содержит число n - число институтов, подавших заявки. Вторая
# строка входного файла содержит n чисел a1, …, an (ai - это количество команд, заявленных от института номер i).
# Последняя строка входного файла содержит число k - количество залов, в которых проходят соревнования.
# Все числа во входном файле целые, положительные и не превосходят 10000.
# Выходные данные - В выходной файл OUTPUT.TXT выведите одно целое число - ответ на задачу.
n = input()
a = map(int, input().split())
k = int(input())
print(sum(k if i > k else i for i in a))
# Или
n = input()
a = map(int, input().split())
k = int(input())
r = 0
for i in a:
    r += k if i > k else i
print(r)
# Или
n = int(input())
a = map(int, input().split())
k = int(input())
r = 0
for i in a:
    if i <= k:
        r += i
    else:
        r += k
print(r)
