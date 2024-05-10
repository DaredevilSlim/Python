#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Листинг 2.2. Применение спецификаторов формата в f-строках
ids = [1, 2, 3]
names = ['Do homework', 'Laundry', 'Pay bills']
urgencies = [5, 3, 4]
for i in range(3):
    print(f'{ids[i]:^12}{names[i]:^12}{urgencies[i]:^12}')  # Применяет спецификаторы формата к выражениям
