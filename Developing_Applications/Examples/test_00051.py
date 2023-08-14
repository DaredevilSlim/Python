#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time    # Подключаем модуля time
import locale  # Подключаем модуля locale

# Форматирование даты и времени
locale.setlocale(locale.LC_ALL, '')
s = "Сегодня:\n%A %d %b %Y %H:%M:%S\n%d.%m.%Y"
print(time.strftime(s))
input()
