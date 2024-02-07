#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Упрощенный способ создания пользовательского исключения
class MyError(Exception):
    pass


try:
    raise MyError('Описание исключения')
except MyError as err:
    print(err)  # Выведет: Описание исключения
