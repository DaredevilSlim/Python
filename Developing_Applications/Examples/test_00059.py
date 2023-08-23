#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Сохранение ссылки на функцию в переменной
def summa(x, y):
    return x + y


f = summa               # Сохраняем ссыпку в переменной f
print(f(10, 20))  # Вызываем функцию через переменную f
