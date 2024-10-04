#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №94 - Принц и дракон
# (Время: 1 сек. Память: 16 Мб Сложность: 22%)
# Волшебник Мерлин продает волшебные мечи принцам, желающим убить дракона. Основная характеристика меча – число
# драконьих голов, которые он срубает за удар. Основная характеристика дракона – число голов, которые он может отрастить
# за сеанс регенерации. Бои принцев с драконами всегда протекают одинаково – принц атакует, и прячется за щитом; дракон
# атакует огненным дыханием и регенерирует; так продолжается до тех пор, пока после очередного удара у дракона не
# кончатся головы. Ясно, впрочем, что не каждым мечом можно победить каждого дракона. Заказ, поступающий Мерлину, всегда
# содержит число голов дракона и скорость его регенерации. Подсчитайте по известной атакующей силе меча, сможет ли принц
# убить такого дракона таким мечом и, если да, то сколько ударов потребуется.
# Входные данные - Единственная строка входного файла INPUT.TXT содержит число N – число голов, которые меч срубает
# одним ударом. Далее идет число M – число голов дракона. За ним идет K – число голов, которые дракон регенерирует за
# раз (1 ≤ N, M, K ≤ 105). Все числа разделены пробелом.
# Выходные данные - В выходной файл OUTPUT.TXT выведите число ударов, которые необходимо нанести принцу, чтобы убить
# дракона, если это возможно. Если таким мечом убить дракона нельзя, то следует вывести «NO».
n, m, k = map(int, input().split())
a = 1
while m - n > 0:
    m -= n - k
    a += 1
    if n <= k:
        a = 'NO'
        m = 0
print(a)
# Или
n, m, k = map(int, input().split())
a = 1
while m - n > 0:
    if n <= k:
        a = 'NO'
        break
    m -= n - k
    a += 1
print(a)
# Или
n, m, k = map(int, input().split())
a = 1
if m > n <= k:
    a = 'NO'
else:
    while m - n > 0:
        m -= n - k
        a += 1
print(a)
# Или
n, m, k = map(int, input().split())
a = 0
if m > n <= k:
    a = 'NO'
else:
    a = 1
    while m - n > 0:
        m -= n - k
        a += 1
print(a)
