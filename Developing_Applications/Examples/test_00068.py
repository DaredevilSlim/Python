#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Декоратор функции
def deco(f):                         # Функция-декоратор
    print('Вызвана функция func()')
    return f                         # Возвращаем ссылку на функцию


@deco
def func(x):
    return 'x = {0}'.format(x)


print(func(10))
