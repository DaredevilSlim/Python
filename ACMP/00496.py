#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №496 - Сбор черники
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по
# окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
# выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# Входные данные - Первая строка входного файла INPUT.TXT содержит целое число N (3 ≤ N ≤ 1000) – количество кустов
# черники. Вторая строка содержит N целых положительных чисел a1, a2, ..., aN – число ягод черники, растущее на
# соответствующем кусте. Все ai не превосходят 1000.
# Выходные данные - В выходной файл OUTPUT.TXT выведите ответ на задачу.
n = int(input())
*a, = map(int, input().split())
print(max((a[i-2] + a[i-1] + a[i]) for i in range(n)))
# Или
n = int(input())
*a, = map(int, input().split())
d = 0
r = 0
for i in range(n):
    d = a[i - 2] + a[i - 1] + a[i]
    if d > r:
        r = d
print(r)
