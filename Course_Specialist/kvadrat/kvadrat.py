#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .solve import solve

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

r = solve(a, b, c)
print(r)

print('END')
