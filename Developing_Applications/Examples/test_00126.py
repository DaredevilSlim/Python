#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Проверочная инструкция
try:
    x = -3
    assert x >= 0, 'Сообщение об ошибке'
except AssertionError as err:
    print(err)  # Выведет: Сообщение об ошибке
