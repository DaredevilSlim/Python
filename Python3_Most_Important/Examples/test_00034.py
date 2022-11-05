#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re  # Подключение модуля re

# Отсутствие привязки к началу или концу строки
p = re.compile(r'[0-9]+', re.S)
if p.search('Строка245'):
    print('Число')  # Выведет: Число
else:
    print('Не число')
input()
