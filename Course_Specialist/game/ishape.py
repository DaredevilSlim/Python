#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import abc
from random import randrange as rand


class IShape(abc.ABC):
    """Интерфейс для реализации геометрических фигур"""

    @abc.abstractmethod
    def get_perimeter(self):
        """Возвращает периметр фигуры"""
        pass

    @abc.abstractmethod
    def get_area(self):
        """Возвращает площадь фигуры"""
        pass

    @abc.abstractmethod
    def get_description(self):
        """Возвращает произвольное описание фигуры"""
        pass


class Circle(IShape):
    Pi = 3.14

    def __init__(self, radius):
        self.__radius = radius

    def get_perimeter(self):
        return 2 * self.__class__.Pi * self.__radius

    def get_area(self):
        return self.__class__.Pi * self.__radius ** 2

    def get_description(self):
        return f'Я - окружность с радиусом {self.__radius}'


class Rectangle(IShape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width
    width = property(get_width)

    def get_height(self):
        return self.__height
    height = property(get_height)

    def get_perimeter(self):
        return (self.__width + self.__height) * 2

    def get_area(self):
        return self.__width * self.__height

    def get_description(self):
        return f'Я - прямоугольник {self.__width}x{self.__height}'


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def get_description(self):
        return f'Я - квадрат со стороной {self.__width}'


class Game:

    question_count = 2

    def __init__(self):
        raise Exception('Нельзя создать экземпляр данного класса')

    @staticmethod
    def __get_shape():
        type_ = rand(3)
        if type_ == 0:
            return Circle(rand(1, 10))
        if type_ == 1:
            return Rectangle(rand(1, 10), rand(1, 10))
        if type_ == 2:
            return Square(rand(1, 10))

    @staticmethod
    def __calculate(string, answer):
        while True:
            guess = input(f'Укажите {string} этой фигуры: ').strip()
            if not guess.replace('.', '', 1).isdigit():
                print('Введите число!')
                continue
            break
        if float(guess) == answer:
            print('Правильно')
        else:
            print(f'Ошибка! Правильный ответ: {answer}')

    @classmethod
    def __run(cls):
        shape = cls.__get_shape()
        if isinstance(shape, IShape):
            print(shape.get_description())
            cls.__calculate('площадь', shape.get_area())
            cls.__calculate('периметр', shape.get_perimeter())
        else:
            raise TypeError('Не та фигура!')

    @classmethod
    def play(cls):
        print(f'Привет! Мы фигуры и у нас есть {cls.question_count} вопроса.')
        while True:
            is_game_over = input('Играем? Y/N').strip()
            if is_game_over.upper() == 'N':
                break
            cls.__run()
        print('Спасибо за участие!')


Game.play()
