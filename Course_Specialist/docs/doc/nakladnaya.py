#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import suppress
from datetime import datetime
import logging

import helpers as hlp
from .position import *

__all__ = ('Nakladnaya',)


class Nakladnaya(object):

    def __init__(self):
        self.__created = datetime.now()
        self.__positions = []

    created = property(lambda self: self.__created)

    @property
    def number(self):
        return self.__number

    @number.setter
    @hlp.info_value
    @hlp.value_not_none
    def number(self, value):
        self.__number = value

    @number.deleter
    def number(self):
        logging.info(f'Number {self.number} deleted')
        del self.__number

    address = property(lambda self: self.__address)

    @address.setter
    @hlp.warning_value
    @hlp.value_not_none
    def address(self, value):
        self.__address = value

    responsible = property(lambda self: self.__responsible)

    @responsible.setter
    @hlp.trace_value(logging.ERROR - 1)
    @hlp.value_not_none
    def responsible(self, value):
        self.__responsible = value

    subscribed = property(lambda self: False)

    @property
    def itogo(self):
        if self.subscribed:
            return self.__itogo
        return sum(p.summa for p in self.__positions)

    def append(self, *args, **kwargs):
        if isinstance(args[0], Position):
            p = args[0]
        else:
            p = Position(*args, **kwargs)
        self.__positions.append(p)

    __str_data = [
        ('Number', 'number'),
        ('Creation date', 'created'),
        ('Address', 'address'),
        ('Responsible person', 'responsible'),
        ('Is subscribed', 'subscribed'),
        ('Result', 'itogo')
    ]

    def __len__(self):
        return len(self.__positions)

    def __str__(self):
        li = []
        for text, prop_name in type(self).__str_data:
            with suppress(AttributeError):
                t = f'{text}: {getattr(self, prop_name)}'
                li.append(t)
        li.extend(map(str, self.__positions))
        return '\n'.join(li)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise ValueError('Slices or keys not supported')
        return self.__positions[key]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise ValueError('Slices or keys not supported')
        self.__positions.append(value)

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise ValueError('Slices or keys not supported')
        del self.__positions[key]

    def __iter__(self):
        yield from self.__positions
