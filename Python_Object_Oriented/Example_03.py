#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В каждом классе существуют магические методы начинающиеся и заканчивающиеся двумя подчеркиваниями

class Point:
    """Класс для предоставления координат точек на плоскости"""
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        # print('вызов __init__ для ' + str(self))
        self.x = x
        self.y = y

    def __del__(self):
        print('Удаление экземпляра: ' + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


# Инициализатор и финализатор
# __init__(self) - инициализатор объекта класса (вызывается сразу после создания объекта класса)
# __del__(self) - финализатор класса (вызывается непосредственно перед удалением объекта класса)
pt = Point()
print(pt.__dict__)
pt.set_coords(1, 2)
print(pt.__dict__)


# Инициализатор __init__
# 1 - Создание объекта (метод __new__)
# 2 - Инициализация объекта (метод __init__)
pt = Point(10, 20)
print(pt.__dict__)
