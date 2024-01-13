#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


# Эта программа показывает случайное число из диапазона от 1 до 10.
def main():
    # Получить случайное число.
    number = random.randint(1, 10)
    # Показать число.
    print(f'Число равняется {number}.')


# Вызвать главную функцию.
main()
