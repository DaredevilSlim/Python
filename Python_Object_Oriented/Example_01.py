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

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


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
