#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №822 - Площадь треугольника
# (Время: 1 сек. Память: 16 Мб Сложность: 15%)
# По целочисленным координатам вершин треугольника (x1,y1), (x2,y2) и (x3,y3) требуется вычислить его площадь.
# Входные данные - Входной файл INPUT.TXT содержит 6 целых чисел x1,y1,x2,y2,x3,y3 – координаты вершин треугольника. Все
# числа не превышают 106 по абсолютной величине.
# Выходные данные - В выходной файл OUTPUT.TXT выведите точное значение площади заданного треугольника.
a, b, c, d, e, f = map(int, input().split())
print(abs(f * (c - a) + d * (a - e) + b * (e - c)) / 2)
# Или
a, b, c, d, e, f = map(int, input().split())
print(abs(a * d - a * f - d * e - c * b + b * e + c * f) / 2)
# Или
a, b, c, d, e, f = map(int, input().split())
print(0.5 * abs((a - e) * (d - f) - (b - f) * (c - e)))