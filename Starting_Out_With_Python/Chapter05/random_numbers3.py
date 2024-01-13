#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


# Эта программа показывает пять случайных чисел из диапазона от 1 до 100.
def main():
    for count in range(5):
        print(random.randint(1, 100))


# Вызвать главную функцию.
main()
