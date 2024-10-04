#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import doc

n = doc.Nakladnaya()

n.append('Рога', 25, unit='шт', price=100.02)
n.append(doc.Position('Копыта', 100, summa=1000.45))

print(n[1])

print('----------------------')
n[2] = doc.Position('Бублики', 21, price=100, summa=1000)
print(n)

print('----------------------')
del n[1]
print(n)

print('----------------------')
for p in n:
    print(p)
