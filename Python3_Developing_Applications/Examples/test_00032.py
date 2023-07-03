#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re  # Подключаем модуль re

# Отсутствие привязки к началу или концу строки
p = re.compile(r'[0-9]+', re.S)
if p.search('Строка245'):
    print('Число')
else:
    print('He число')  # Выведет: Число
input()
