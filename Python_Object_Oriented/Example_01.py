#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# getattr(obj, name [, default]) - возвращает значение атрибута объекта;
# hasattr(obj, name) - проверяет на наличие атрибута name в object;
# setattr(obj, name, value) - задает значение атрибута (если атрибут не существует, то он создается);
# delattr(obj, name) - удаляет атрибут с именем name;
# __doc__ - содержит строку с описанием класса;
# __dict__ - содержит набор атрибутов экземпляра класса;


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


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = 0
        self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


print(Point.__dict__)
# Создание нового атрибута класса setattr
setattr(Point, 'prop', 1)
print(Point.__dict__)

# Проверка наличия атрибута в классе getattr
print(getattr(Point, 'prop', False))
print(getattr(Point, 'test', False))

# Проверка наличия атрибута в классе hasattr (для экземпляров класса проверяется наличие так же и в самом классе)
print(hasattr(Point, 'prop'))

# Удаление атрибута из класса del
del  Point.prop
print(getattr(Point, 'prop', False))
print(hasattr(Point, 'prop'))

# Удаление атрибута из класса delattr
setattr(Point, 'prop', 3)
print(getattr(Point, 'prop', False))
print(hasattr(Point, 'prop'))
delattr(Point, 'prop')
print(getattr(Point, 'prop', False))
print(hasattr(Point, 'prop'))

a = Point()
b = Point()
a.x = 1
a.y = 1
b.x = 10
b.y = 20

print(Point.__doc__)

pt = Point()
pt2 = Point()
pt.set_coords(1, 2)
pt2.set_coords(10, 20)
print(pt.__dict__)
print(pt2.__dict__)
print(pt.get_coords())
print(pt2.get_coords())
f = getattr(pt, 'get_coords')
f2 = getattr(pt2, 'get_coords')
print(f)
print(f2)
print(f())
print(f2())


# Инициализатор и финализатор
# __init__(self) - инициализатор объекта класса (вызывается сразу после создания объекта класса)
# __del__(self) - финализатор класса
pt = Point()
print(pt.__dict__)

# Инициализатор __init__
# 1 - Создание объекта (метод __new__)
# 2 - Инициализация объекта (метод __init__)
pt = Point(1, 2)
print(pt.__dict__)


# Магический метод __new__
# __new__() - вызывается перед созданием объекта класса
pt = Point(1, 2)
print(pt)

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(id(db), id(db2))


# Декораторы @classmethod и @staticmethod
v = Vector(1, 2)
res = v.get_coord()
print(res)
res = Vector.get_coord(v)
print(res)
res = Vector.validate(5)
print(res)
v = Vector(1, 2)
res = v.get_coord()
print(res)
v = Vector(1, 200)
res = v.get_coord()
print(res)
res = Vector.norm2(5, 6)
print(res)
