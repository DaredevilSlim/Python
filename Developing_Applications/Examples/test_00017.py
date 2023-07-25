#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Инструкция выбора
print('''Какой операционной системой вы пользуетесь?
1 - Windows 11
2 - Windows 10
3 - Windows 8.1
4 - Windows 8
5 - Windows 7
6 - Другая''')
os = input('Введите число, соответствующее ответу: ')
match os:
    case '1':
        print('Вы выбрали: Windows 11')
    case '2':
        print('Вы выбрали: Windows 10')
    case 'З':
        print('Bы выбрали: Windows 8.1')
    case '4':
        print('Bы вы6рали: Windows 8')
    case '5':
        print('Вы вы6рали: Windows 7')
    case '6':
        print('Bы вы6рали: другая')
    case '':
        print('Bы не ввели число')
    case _:
        print('Мы не смогли определить вашу операционную систему')
input()
