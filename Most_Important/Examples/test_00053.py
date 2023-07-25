#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import strftime     # Подключение функции strftime() из модуля time
from locale import setlocale  # Подключение функции setlocale() из модуля locale
from locale import LC_ALL     # Подключение функции LC_ALL() из модуля locale

# Форматирование даты и времени
setlocale(LC_ALL, "Russian_Russia.1251")
s = "Сегодня:\n%А %d %Ь %У %H:%M:%S\n%d.%m.%Y"
print(strftime(s))
input()
