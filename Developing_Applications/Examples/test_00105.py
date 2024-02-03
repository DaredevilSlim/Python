#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


# Абстрактный метод
class Class1(ABC):
    @abstractmethod  # Абстрактный метод
    def func(self, x):
        pass


class Class2(Class1):
    def func(self, x):  # Перекрываем абстрактный метод
        print(x)


class Class3(Class1):  # Класс не перекрывает абстрактный метод
    pass


c2 = Class2()
c2.func(50)  # Выведет: 50
try:
    c3 = Class3()  # Ошибка. Метод func() не перекрыт
    c3.func(50)
except TypeError as msg:
    print(msg)  # Can't instantiate abstract class Class3 without an implementation for abstract method 'func'
