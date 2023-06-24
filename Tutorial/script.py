#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sum = 0
for i in range(1, 100000000):
    sum += (2 * i - 1)
    if sum != i ** 2:
        print(i, 'False')
print(sum)
