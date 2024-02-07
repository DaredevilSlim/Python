#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Применение четвертого формата конструкции raise
class MyError(Exception):
    pass


try:
    raise MyError('Сообщение об ошибке')
except MyError as err:
    print(err)
    raise   # Повторно генерируем исключение
