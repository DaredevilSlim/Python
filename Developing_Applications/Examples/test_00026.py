#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Оператор присваивания в составе инструкции
print("Введите слово 'stop' для получения результата")
summa = 0
while (x := input('Введите число: ')) != 'stop':
    x = int(x)
    summa += x
print('Сумма чисел равна:', summa)
input()
