#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использование примеси
class Mixin:  # Определяем сам класс-примесь
    attr = 0  # Определяем атрибут примеси

    def mixin_method(self):  # Определяем метод примеси
        print('Метод примеси')


class Class1(Mixin):
    def method_one(self):
        print('Метод класса Class1')


class Class2 (Class1, Mixin):
    def method_two(self):
        print('Метод класса Class2')


c1 = Class1()
c1.method_one()
c1.mixin_method()  # Class1 поддерживает метод примеси
c2 = Class2()
c2.method_one()
c2.method_two()
c2.mixin_method()  # Class2 также поддерживает метод примеси
