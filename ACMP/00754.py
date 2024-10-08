#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №754 - Три толстяка
# (Время: 1 сек. Память: 16 Мб Сложность: 7%)
# Три толстяка решили поспорить: кто из них самый тяжелый. После взвешивания оказалось, что их масса соответственно M1,
# M2 и M3 килограмм. Считается, что масса толстяка должна быть не менее 94 и не более 727 килограмм.
# Помогите определить массу самого тяжелого из них, либо выяснить, что была допущена ошибка при взвешивании.
# Входные данные - Входной файл INPUT.TXT содержит три целых числа M1, M2 и M3, разделенные пробелом. Все числа целые и
# не превосходят 10 000 по абсолютной величине.
# Выходные данные - В выходной файл OUTPUT.TXT выведите массу самого тяжелого толстяка в случае корректного взвешивания,
# либо слово «Error» в противном случае.
a = sorted(list(map(int, input().split())))
print(a[2] if a[0] > 93 and a[2] < 728 else 'Error')
