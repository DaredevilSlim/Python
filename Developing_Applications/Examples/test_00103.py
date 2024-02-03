#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Статистические методы
class MyClass:
    @staticmethod
    def func_one(x, y):  # Статический метод
        return x + y

    def func_two(self, x, y):  # Обычный метод
        return x + y

    def func_three(self, x, y):
        return MyClass.func_one(x, y)  # Вызов статического метода из обычного


print(MyClass.func_one(10, 20))  # Вызываем статический метод
c = MyClass()
print(c.func_two(15, 6))         # Вызываем обычный метод
print(c.func_one(50, 12))        # Вызываем статический метод через объект
print(c.func_three(23, 5))       # Вызываем обычный метод, вызывающий статический метод
