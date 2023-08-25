#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Указание нескольких декораторов
def deco1(f):
    print('Вызвана функция deco1()')
    return f


def deco2(f):
    print('Вызвана функция deco2()')
    return f


@deco1
@deco2
def func(x):
    return 'x = {0}'.format(x)


print(func(10))
