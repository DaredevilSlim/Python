#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Сортировка без учета регистра символов
arr = ['единица1', 'Единый', 'Единица2']
arr.sort(key=lambda s: s.lower())
for i in arr:
    print(i, end=' ')
# Результат выполнения: единица1 Единица2 Единый
