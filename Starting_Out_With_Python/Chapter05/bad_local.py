#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Определение главной функции.
def main():
    get_name()
    print(f'Привет {name}.')  # Эта инструкция вызовет ошибку!


# Определение функции get_name.
def get_name():
    name = input('Введите свое имя: ')


# Вызвать главную функцию.
main()
