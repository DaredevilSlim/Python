#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №148 - НОД
# (Время: 1 сек. Память: 16 Мб Сложность: 15%)
# Даны два натуральных числа A и B. Требуется найти их наибольший общий делитель (НОД).
# Входные данные - Во входном файле INPUT.TXT в единственной строке записаны натуральные числа A и B через пробел
# (A, B ≤ 109).
# Выходные данные - В выходной файл OUTPUT.TXT выведите НОД чисел А и В.


def nod(n, m):
    x = n % m
    y = m % n
    return m if x == 0 else nod(m, x) if n >= m else n if y == 0 else nod(n, y)


a, b = map(int, input().split())
print(nod(a, b))


# Или
def nod(n, m):
    if n >= m:
        return m if (n % m) == 0 else nod(m, (n % m))
    return n if (m % n) == 0 else nod(n, (m % n))


a, b = map(int, input().split())
print(nod(a, b))


# Или
def gcd(aa, bb):
    if aa >= bb:
        if (aa % bb) == 0:
            return bb
        return gcd(bb, (aa % bb))
    else:
        if (bb % aa) == 0:
            return aa
        return gcd(aa, (bb % aa))


a, b = map(int, input().split())
print(gcd(a, b))
