#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Упорядоченный вывод элементов словаря с помощью метода sorted()
d = {'z': 3, 'y': 2, 'x': 1}
for key in sorted(d.keys()):
    print('({0} => {1})'.format(key, d[key]), end=' ')
# Выведет: (x => 1) (y => 2) (z => 3)
