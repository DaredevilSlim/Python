#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Переопределение методов
class Class1:
    def __init__(self):
        print('Конструктор базового класса')

    def func_one(self):
        print('Метод func_one() класса Class1')

    def func_two(self):
        print('Метод func_two() класса Class1')


class Class2(Class1):
    def __init__(self):
        print('Конструктор производного класса')
        Class1.__init__(self)  # Вызываем конструктор базового класса

    def func_one(self):
        print('Метод func_one() класса Class2')
        super().func_one()  # Вызываем метод базового класса

    def func_two(self):
        print('Метод func_two() класса Class2')
        super(Class2, self).func_two()  # Вызываем метод базового класса


c = Class2()    # Создаем объект класса Class2
c.func_one()    # Выведет: Вызываем метод func_one()
c.func_two()    # Выведет: Вызываем метод func_two()
