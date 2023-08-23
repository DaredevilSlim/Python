#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Функции обратного вызова
def summa(x, y):
    return x + y


def func(f, a, b):
    """ Через переменную f будет доступна ссыпка на функцию summa() """
    return f(a, b)   # Вызываем функцию summa()


# Передаем ссыпку на функцию в качестве параметра
print(func(summa, 10, 20))
