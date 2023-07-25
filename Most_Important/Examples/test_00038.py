#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re  # Подключение модуля re


# Поиск чисел в строке
def repl(m):
    """Функция для замены. m - объект Match"""
    x = int(m.group(0))
    x += 10
    return '{0}'.format(x)


p = re.compile(r'[0-9]+')
# Замена всех вхождений
print(p.sub(repl, '2008, 2009, 2010, 2011'))
# Замена только первых двух вхождений
print(p.sub(repl, '2008, 2009, 2010, 2011', 2))
input()
