#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №233 - Автобусная экскурсия
# (Время: 1 сек. Память: 16 Мб Сложность: 14%)
# Оргкомитет Московской городской олимпиады решил организовать обзорную экскурсию по Москве для участников олимпиады.
# Для этого был заказан двухэтажный автобус (участников олимпиады достаточно много и в обычный они не умещаются) высотой
# 437 сантиметров. На экскурсионном маршруте встречаются N мостов. Жюри и оргкомитет олимпиады очень обеспокоены тем,
# что высокий двухэтажный автобус может не проехать под одним из них. Им удалось выяснить точную высоту каждого из
# мостов. Автобус может проехать под мостом тогда и только тогда, когда высота моста превосходит высоту автобуса.
# Помогите организаторам узнать, закончится ли экскурсия благополучно, а если нет, то установить, где произойдет авария.
# Входные данные - Во входном файле INPUT.TXT сначала содержится число N (1 ≤ N ≤ 1000). Далее идут N натуральных чисел,
# не превосходящих 10000 - высоты мостов в сантиметрах в том порядке, в котором они встречаются на пути автобуса.
# Выходные данные - В единственную строку выходного файла OUTPUT.TXT нужно вывести фразу "No crash", если экскурсия
# закончится благополучно. Если же произойдет авария, то нужно вывести сообщение "Crash k", где k - номер моста, где
# произойдет авария. Фразы выводить без кавычек ровно с одним пробелом внутри.
n = int(input())
k = input().split()
i = 0
while n != 0 and int(k[i]) > 437:
    n -= 1
    i += 1
print(f'Crash {i + 1}' if n else 'No crash')
# Или
n = int(input())
k = input().split()
i = 0
while n != 0 and int(k[i]) > 437:
    n -= 1
    i += 1
print('No crash' if n == 0 else 'Crash %d' % (i + 1))
# Или
n = int(input())
k = [int(i) for i in input().split()]
i = 0
while n != 0 and k[i] > 437:
    n -= 1
    i += 1
print('No crash' if n == 0 else 'Crash ' + str(i + 1))
