#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа демонстрирует, что происходит, когда вы изменяете значение параметра.
def main():
    value = 99
    print(f'Значение равно {value}.')
    change_me(value)
    print(f'После возвращения в функцию main значение равно {value}.')


def change_me(arg):
    print('Я изменяю значение.')
    arg = 0
    print(f'Теперь значение равно {arg}.')


# Вызвать главную функцию.
main()
