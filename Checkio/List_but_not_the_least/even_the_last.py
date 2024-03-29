#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту
# сумму и последний элемент исходного массива. Не забудьте, что первый элемент массива имеет индекс 0.
# Для пустого массива результат всегда 0 (ноль).
# Входные данные: Список (list) целых чисел (int).
# Выходные данные: Число как целочисленное (int).
# Зачем это нужно: Индексы и срезы - очень важные элементы программирования, как на Python, так и на других языках.
# Это поможет вам в дальнейшем.
# Предусловия: 0 ≤ len(array) ≤ 20
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)
def checkio(array: list[int]) -> int:
    return 0 if array == [] else sum(i for i in array[::2]) * array[-1]


print(checkio([0, 1, 2, 3, 4, 5]))  # 30
print(checkio([1, 3, 5]))           # 30
print(checkio([6]))                 # 36
print(checkio([]))                  # 0
