#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №131 - Перепись
# (Время: 1 сек. Память: 16 Мб Сложность: 15%)
# В доме живет N жильцов. Однажды решили провести перепись всех жильцов данного дома и составили список, в котором
# указали возраст и пол каждого жильца. Требуется найти номер самого старшего жителя мужского пола.
# Входные данные - Во входном файле INPUT.TXT в первой строке задано натуральное число N – количество жильцов (N ≤ 100).
# В последующих N строках располагается информация о всех жильцах: каждая строка содержит два целых числа:
# V и S – возраст и пол человека (1 ≤ V ≤ 100, S – 0 или 1). Мужскому полу соответствует значение S=1, а женскому – S=0.
# Выходные данные - Выходной файл OUTPUT.TXT должен содержать номер самого старшего мужчины в списке. Если таких жильцов
# несколько, то следует вывести наименьший номер. Если жильцов мужского пола нет, то выведите -1.
n = int(input())
w = 0
e = -1
i = 1
while i < n + 1:
    v, s = map(int, input().split())
    if v > w and s > 0:
        w = v
        e = i
    i += 1
print(e)
# Или
n = int(input())
w = 0
e = -1
for i in range(1, n + 1):
    v, s = map(int, input().split())
    if v > w and s == 1:
        w = v
        e = i
print(e)
