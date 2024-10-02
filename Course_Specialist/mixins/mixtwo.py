#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ('func_1', 'z',)


def func_1(self, m):
    print('func_1', 2 * m)


def method_1(self):
    print('Какая-то фигня на постном масле')


z = property(lambda self: self.var)

z.setter


def z(self, value):
    self.var = value

