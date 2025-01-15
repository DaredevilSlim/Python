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


Point.color = 'black'
print(Point.circle)
print(Point.__dict__)
a = Point()
b = Point()
print(type(a) == Point)
print(isinstance(a, Point))
Point.circle = 1
print(Point.__dict__)
print(a.color)
print(b.circle)
a.color = 'green'
print(a.color, b.color)
Point.type_pt = 'disc'
print(Point.__dict__)

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

print(a.__dict__)
print(b.__dict__)

print(Point.__doc__)
