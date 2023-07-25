#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re  # Подключаем модуль re

# Суммирование произвольного количества чисел
print("Введите слово 'stop' для получения результата")
summa = 0
p = re.compile(r'^[-]?[0-9]+$', re.S)
while (x := input('Введите число: ')) != 'stop':
    if not p.search(x):
        print('Необходимо ввести число, а не строку!')
        continue                                        # Переходим на следующую итерацию цикла
    x = int(x)                                          # Преобразуем строку в число
    summa += x
print('Сумма чисел равна:', summa)
input()
