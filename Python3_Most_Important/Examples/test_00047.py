#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Пользовательская сортировка
arr = ['единица1', 'Единый', 'Единица2']
arr.sort(key=str.lower)  # Указываем метод lower()
for i in arr:
    print(i, end=' ')
# Результат выполнения: единица1 Единица2 Единый
