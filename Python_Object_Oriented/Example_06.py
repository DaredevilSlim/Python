#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from accessify import private, protected

# Механизм инкапсуляции
# attribute (без одного или двух подчеркиваний вначале) - публичное свойство (public).
# _attribute (с одним подчеркиванием) - режим доступа protected (служит для обращения внутри класса и во всех его
# дочерних классах).
# __attribute (с двумя подчеркиваниями) - режим доступа private (служит для обращения только внутри класса).
# Для лучшей защиты методов класса от доступа извне необходимо использовать модуль accessify
# python3.13 -m pip install -U accessify

class Point:
    def __init__(self, x=0, y=0):
        self.__x = 0
        self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    # приватный метод __check_value
    # @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    # setter (сеттер) - интерфейсный метод
    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            # приватные локальные свойства
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    # getter (геттер) - интерфейсный метод
    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coord())
print(dir(pt))
