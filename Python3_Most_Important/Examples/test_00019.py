#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вложенные инструкции
print("""Какой операционной системой вы пользуетесь?
    1 - Windows 10
    2 - Windows 8.1
    3 - Windows 8
    4 - Windows 7
    5 - Windows Vista
    6 - Другая""")
os = input('Введите число, соответствующее ответу: ')
if os != '':
    if os == '1':
        print('Вы выбрали: Windows 10')
    elif os == '2':
        print('Вы выбрали: Windows 8.1')
    elif os == '3':
        print('Вы выбрали: Windows 8')
    elif os == '4':
        print('Вы выбрали: Windows 7')
    elif os == '5':
        print('Вы выбрали: Windows Vista')
    elif os == '6':
        print('Вы выбрали: другая')
    else:
        print('Мы не смогли определить вашу операционную систему')
elif not os:
    print('Вы не ввели число')
input()
