#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

# Эта программа имитирует 10 бросков монеты.
# Константы.
HEADS = 1  # Орел.
TAILS = 2  # Решка.
TOSSES = 10  # Количество бросков.


def main():
    for toss in range(TOSSES):
        # Имитировать бросание монеты.
        if random.randint(HEADS, TAILS) == HEADS:
            print('Орел')
        else:
            print('Решка')


# Вызвать главную функцию.
main()
