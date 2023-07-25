#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Оператор continue
for i in range(1, 101):
    if 4 < i < 11:
        continue         # Переходим на следующую итерацию цикла
    print(i)
