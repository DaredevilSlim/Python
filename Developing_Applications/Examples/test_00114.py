#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Обработка нескольких исключений
try:
    x = 1 / 0
except (NameError, IndexError, ZeroDivisionError) as err:  # Обработка одновременно нескольких исключений
    x = 0

print(x)  # Выведет: 0
