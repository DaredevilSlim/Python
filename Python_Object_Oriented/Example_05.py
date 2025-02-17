#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Обычные методы класса - вызываются из экземпляров класса и позволяют работать как с атрибутами экземпляра (посредством
# параметра self), так и с атрибутами самого класса
# @classmethod - позволяет работать только с атрибутами класса (отсутствует возможность работы с локальными свойствами
# экземпляра класса, так как отсутствует ссылка на соответствующий экземпляр)
# @staticmethod - позволяет создать независимую сервисную функцию, работающую исключительно с параметрами, которые
# определены в этой функции (отсутствует возможность обращения к атрибутам класса, а так же к локальным свойствам
# экземпляра класса)


class Vector:
    # Атрибуты класса Vector
    MIN_COORD = 0
    MAX_COORD = 100

    # Метод класса Vector
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = 0
        self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))

    def get_coords(self):
        return self.x, self.y

    # Статический метод класса Vector
    # Функция вычисления квадратичной нормы
    @staticmethod
    def norm2(x, y):
        return x * x + y * y


v = Vector(1, 2)
print(v.validate(5))
res = v.get_coords()
print(res)
v = Vector(1, 200)
res = v.get_coords()
print(res)
v = Vector(10, 20)
print(v.norm2(5, 6))
res = v.get_coords()
print(res)
print(Vector.validate(5))
res2 = Vector.get_coords(v)
print(res2)
