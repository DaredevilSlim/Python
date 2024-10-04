#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Point(object):

    # attributes of class Point
    __count = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        Point.__count += 1

    @classmethod
    def count_points(cls):
        return f'Количество экземпляров класса Point - {cls.__count}'

    def move_to(self, x, y):
        self.__x = x
        self.__y = y

    def move_by(self, x, y):
        self.__x += x
        self.__y += y

    def __repr__(self):
        return f'Я - точка: {self.__x} x {self.__y}'

    # property for x
    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    x = property(get_x, set_x)

    # property for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


point = Point(10, 20)
print(point)  # Я - точка: 10 x 20

point.move_to(100, 200)
print(point)  # Я - точка: 100 x 200

point.move_by(10, 20)
print(point.x, ':', point.y)  # 110 : 220

point.x = 30
point.y = 40
print(point)  # Я - точка: 30 x 40

print(Point.count_points())  # Количество экземпляров класса Point - 1
