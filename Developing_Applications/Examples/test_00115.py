#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Получение сведений исключений
try:
    x = 1 / 0                      # Ошибка деления на ноль
except (NameError, IndexError, ZeroDivisionError) as err:
    print(err.__class__.__name__)  # Имя класса исключения
    print(err)                     # Текст сообщения об ошибке
