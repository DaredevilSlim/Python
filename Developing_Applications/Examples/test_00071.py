#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ограничение доступа с помощью декоратора
passw = input('Введите пароль: ')


def test_passw(p):
    def deco(f):
        if p == '10':  # Сравниваем пароли
            return f
        else:
            return lambda: 'Доступ закрыт'  # Возвращаем функцию-декоратор
    return deco


@test_passw(passw)
def func():
    return 'Доступ открыт'


print(func())
# Вызываем функцию
