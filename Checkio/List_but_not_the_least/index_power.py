#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дан массив с положительными числами и число N. Вы должны найти N-ую степень элемента в массиве с индексом N. Если N
# за границами массива, тогда вернуть -1. Не забывайте, что первый элемент имеет индекс 0.
# Давайте посмотрим на несколько примеров:
# - массив = [1, 2, 3, 4] и N = 2, тогда результат 3 2 == 9;
# - массив = [1, 2, 3] и N = 3, но N за границами массива, так что результат -1.
# Входные значения: Два агумента. Массив как список целых и число как целое.
# Выходные значения: Целое число.
# Как это используется: Эта миссия учит вас как использовать основы массивов и индексов в объединении с простой
# математикой.
# Предусловие: 0 < len(array) ≤ 10
# 0 ≤ N
# all(0 ≤ x ≤ 100 for x in array)
def index_power(array: list, n: int) -> int:
    return pow(array[n], n) if len(array) > n else -1


print(index_power([1, 2, 3, 4], 2))     # 9
print(index_power([1, 3, 10, 100], 3))  # 1000000
print(index_power([0, 1], 0))           # 1
print(index_power([1, 2], 3))           # -1
