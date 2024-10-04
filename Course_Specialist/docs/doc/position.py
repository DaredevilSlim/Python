#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import suppress
from decimal import Decimal

__all__ = ('Position',)


class Position(object):

    def __init__(self, title, quantity, **kwargs):
        self.__title = title
        self.__quantity = quantity
        with suppress(KeyError):
            self.__unit = kwargs['unit']
        with suppress(KeyError):
            self.__price = Decimal(kwargs['price'])
        try:
            self.__summa = Decimal(kwargs['summa'])
        except KeyError:
            try:
                self.__summa = self.quantity * self.price
            except AttributeError as Exc:
                raise ValueError('Price or summa have to be specified') from Exc

    title = property(lambda self: self.__title)
    quantity = property(lambda self: self.__quantity)
    unit = property(lambda self: self.__unit)
    price = property(lambda self: self.__price)
    summa = property(lambda self: self.__summa)

    def __str__(self):
        li = [self.title]
        with suppress(AttributeError):
            li.append(self.unit)
        li.append(f'c: {self.quantity}')
        with suppress(AttributeError):
            li.append(f'p: {self.price}')
        li.append(f's: {self.summa}')
        return ' '.join(li)

