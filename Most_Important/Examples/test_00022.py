#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Пример использования функции enumerate()
arr = [1, 2, 3, 4, 5, 6]
for i, elem in enumerate(arr):
    if elem % 2 == 0:
        arr[i] *= 2
print(arr)  # Результат выполнения: [1, 4, 3, 8, 5, 12]
