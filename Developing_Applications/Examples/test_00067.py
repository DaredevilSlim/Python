#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вызов одной функции-генератора из другой (сложный случай)
def gen2(n):
    for e in range(1, n + 1):
        yield e * 2


def gen(l):
    for e in l:
        yield from gen2(e)


l = [5, 10]
for i in gen([5, 10]):
    print(i, end=' ')
