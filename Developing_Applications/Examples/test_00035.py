#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re  # Подключаем модуль re

# Проверка e-mail на соответствие шаблону
email = input('Введите e-mail: ')
pe = r'^([a-z0-9_.-]+)@(([a-z0-9-]+\.)+[a-z]{2,6})$'
p = re.compile(pe, re.I | re.S)
m = p.search(email)
if not m:
    print('E-mail не соответствует шаблону')
else:
    print('E-mail', m.group(0), 'соответствует шаблону')
    print('ящик:', m.group(1), 'домен:', m.group(2))
input()
