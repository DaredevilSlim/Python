#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Методы класса
class MyClass:
    @classmethod
    def func(cls, x):  # Метод класса
        print(cls, x)


MyClass.func(10)  # Вызываем метод класса у класса
c = MyClass()
c.func(50)        # Вызываем метод класса у объекта
