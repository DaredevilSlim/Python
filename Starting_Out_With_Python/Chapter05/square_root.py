#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


# Эта программа демонстрирует функцию sqrt.
def main():
    # Получить число.
    number = float(input('Введите число: '))
    # Получить квадратный корень числа.
    square_root = math.sqrt(number)
    # Показать квадратный корень.
    print(f'Квадратный корень из {number} составляет {square_root}.')


# Вызвать главную функцию.
main()
