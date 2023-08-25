#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Языковая конструкция nonlocal
def func1(a):
    x = a

    def func2(b):
        nonlocal x  # Объявляем переменную как nonlocal
        print(x)
        x = b       # Можем изменить значение х в func1()
    return func2


f = func1(10)
f(5)   # Выведет: 10
f(12)  # Выведет: 5
f(3)   # Выведет: 12
