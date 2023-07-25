#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Пример использования функции filter()
def func(elem):
    return elem >= 0


arr = [-1, 2, -3, 4, 0, -20, 10]
arr = list(filter(func, arr))
print(arr)  # Результат: [2, 4, О, 10]

# Использование генераторов списков
arr = [-1, 2, -3, 4, 0, -20, 10]
arr = [i for i in arr if func(i)]
print(arr)  # Результат: [2, 4, О, 10]
