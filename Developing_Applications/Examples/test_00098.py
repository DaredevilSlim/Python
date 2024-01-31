#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Указание класса при наследовании метода
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
    # Наследуем func_two() из класса Class3, а не из класса Class2
    func_two = Class3.func_two
    
    def func_four(self):
        print('Метод func_four() класса Class4')


print(Class1.__bases__)
print(Class2.__bases__)
print(Class3.__bases__)
print(Class4.__bases__)
