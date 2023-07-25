#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Функция map()
def func(elem):
    """ Увеличенное значение каждого элемента списка """
    return elem + 10  # Возвращаем новое значение


arr = [1, 2, 3, 4, 5]
print(list(map(func, arr)))
# Результат выполнения: [11, 12, 13, 14, 15]
