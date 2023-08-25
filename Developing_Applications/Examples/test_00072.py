#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вычисление факториала
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


while True:
    x = input('Введите число: ')
    if x.isdigit():  # Если строка содержит только цифры
        x = int(x)   # Преобразуем строку в число
        break        # Выходим из цикла
    else:
        print('Bы ввели не число!')
print('Факториал числа {0} = {1}'.format(x, factorial(x)))
