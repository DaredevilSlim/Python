#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Оператор continue
for i in range(1, 11):
    if 3 < i < 8:
        continue  # Переход на следующую итерацию цикла
    print(i)
