#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №26 - Две окружности
# (Время: 1 сек. Память: 16 Мб Сложность: 17%)
# На плоскости даны две окружности. Требуется проверить, пересекаются ли они.
# Входные данные - Входной файл INPUT.TXT состоит из двух строк. На каждой строке записана информация об одной
# окружности – координаты ее центра x и y (целые числа, по модулю не превосходящие 5000) и радиус
# (целое число 1 ≤ r ≤ 1000).
# Выходные данные - В выходной файл OUTPUT.TXT выведите «YES», если окружности пересекаются, и «NO» в противном случае.
a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
g = abs(a - d + b - e)
print('YES' if c + f >= g and c + g >= f and f + g >= c else 'NO')
# Или
a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
g = ((a - d) ** 2 + (b - e) ** 2) ** .5
print('YES' if c + f >= g and c + g >= f and f + g >= c else 'NO')
