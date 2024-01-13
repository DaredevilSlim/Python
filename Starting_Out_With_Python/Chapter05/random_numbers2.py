#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


# Эта программа показывает пять случайных чисел из диапазона от 1 до 100.
def main():
    for count in range(5):
        # Получить случайное число.
        number = random.randint(1, 100)
        # Показать число.
        print(number)


# Вызвать главную функцию.
main()
