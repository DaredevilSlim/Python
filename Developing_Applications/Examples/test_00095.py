#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Наследование
class Class1:  # Базовый класс
    def func_one(self):
        print('Метод func_one() класса Class1')

    def func_two(self):
        print('Метод func_two() класса Class1')


class Class2(Class1):  # Производный класс Class2 наследует класс. Class1
    def func_two(self):
        print('Метод func_two() класса Class2 перекрыл метод класса Class1')

    def func_three(self):
        print('Метод func_three() класса Class2')


c1 = Class1()    # Создаем объект класса Class1
c2 = Class2()    # Создаем объект класса Class2
c2.func_one()    # Выведет: Метод func_one() класса Class1
c1.func_two()    # Выведет: Метод func_two() класса Class1
c2.func_two()    # Выведет: Метод func_two() класса Class2 перекрыл метод класса Class1
c2.func_three()  # Выведет: Метод funcЗ() класса Class2
