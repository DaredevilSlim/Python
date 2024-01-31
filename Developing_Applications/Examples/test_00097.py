#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Множественное наследование
class Class1:  # Базовый класс для класса Class2
    def func_one(self):
        print('Метод func_one() класса Class1')


class Class2(Class1):  # класс Class2 наследует класс Class1
    def func_two(self):
        print('Метод func_two() класса Class2')


class Class3(Class1):  # класс Class3 наследует класс Class1
    def func_one(self):
        print('Метод func_one() класса Class3')
        
    def func_two(self):
        print('Метод func_two() класса Class3')

    def func_three(self):
        print('Метод func_three() класса Class3')

    def func_four(self):
        print('Метод func_four() класса Class3')


class Class4(Class2, Class3):  # Множественное наследование
    def func_four(self):
        print('Метод func_four() класса Class4')


c = Class4()    # Создаем объект класса Class4
c.func_one()    # Выведет: Метод func_one() класса Class3
c.func_two()    # Выведет: Метод func_two() класса Class2
c.func_three()  # Выведет: Метод func_three() класса Class3
c.func_four()   # Выведет: Метод func_four() класса Class4
