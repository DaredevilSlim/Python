#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from mymix import my_mix
import mixtwo
from mixin import mixin


@mixin(mixtwo)
class MyClass(object):

    def method_1(self):
        print('method_1')

    def method_2(self):
        print('method_2')

    x = property(lambda self: self.__x)


    @x.setter
    def x(self, value):
        self.__x = value


a = MyClass()
a.x = 10
print(a.x)

print(a._MyClass__x)
a._MyClass__x = 25
print(a._MyClass__x)
