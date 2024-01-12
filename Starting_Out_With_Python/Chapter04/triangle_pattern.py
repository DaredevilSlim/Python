#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа выводит треугольную комбинацию.
BASE_SIZE = 8
for r in range(BASE_SIZE):
    for c in range(r + 1):
        print('*', end='')
    print()
