#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Магический метод __new__() - вызывается перед созданием объекта класса
# Атрибут cls магического метода __new__() ссылается на текущий класс (Point)
# super() - ссылка на базовый класс
# Атрибут self ссылается на конкретный экземпляр класса.
# Начиная с версии 3 в Python все классы наследуются от системного базового класса object.

class Point:
    """Класс для предоставления координат точек на плоскости"""
    color = 'red'
    circle = 2

    def __new__(cls, *args, **kwargs):
        print('вызов __new__ для ' + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print('вызов __init__ для ' + str(self))
        self.x = x
        self.y = y

    def __del__(self):
        print('Удаление экземпляра: ' + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point(1, 2)
print(pt)


# Паттерн программирования Singleton

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('закрытие соединения с БД')

    def read(self):
        return 'данные из БД'

    def write(self, data):
        print(f'запись в БД {data}')


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(id(db), id(db2))
