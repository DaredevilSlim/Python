#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mix_1(self):
    print('mix_1', self.x)


y = property(lambda self: 'y')


def my_mix(cls):
    setattr(cls, 'mix_1', mix_1)
    setattr(cls, 'y', y)
    return cls
