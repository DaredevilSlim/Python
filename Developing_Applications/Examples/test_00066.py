#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вызов одной функции-генератора из другой (простой случай)
def gen(l):
    for e in l:
        yield from range(1, e + 1)


l = [5, 10]
for i in gen([5, 10]):
    print(i, end=' ')
