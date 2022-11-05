#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Перебор элементов списка
arr = [1, 2, 3]
i, count = 0, len(arr)
while i < count:
    arr[i] *= 2
    i += 1
print(arr)  # Результат выполнения: [2, 4, 6]
