#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re  # Подключаем модуль re


# Поиск чисел в строке
def rep1(m):
    """ Функция дпя замены. m - объект Match """
    x = int(m.group(0))
    x += 10
    return '{0}'.format(x)


p = re.compile(r'[0-9]+')
# Заменяем все вхождения
print(p.sub(rep1, '2019, 2020, 2021, 2022'))
# Заменяем только первые два вхождения
print(p.sub(rep1, '2019, 2020, 2021, 2022', 2))
input()
