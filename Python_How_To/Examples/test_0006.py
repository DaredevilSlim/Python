#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Листинг 2.6. Методы объекта Match
match = re.search(r'(\w\d)+', 'xyza2b1c3dd')
print('matched:', match.group())                       # Вывод: matched: a2b1c3
print('span:', match.span())                           # Вывод: span: (3, 9)
print(f'start: {match.start()} & end: {match.end()}')  # Вывод: start: 3 & end: 9
