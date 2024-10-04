#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №757 - Спирт
# (Время: 1 сек. Память: 16 Мб Сложность: 10%)
# Каждому школьнику из курса органической химии известна формула молекулы этилового спирта – C2H5(OH). Откуда видно, что
# молекула спирта состоит из двух атомов углерода (C), шести атомов водорода (H) и одного атома кислорода (O).
# По заданному количеству атомов каждого из описанных выше элементов требуется определить максимально возможное
# количество молекул спирта, которые могут образоваться в процессе их соединения.
# Входные данные - Первая строка входного файла INPUT.TXT содержит 3 натуральных числа: C, Н и O – количество атомов
# углерода, водорода и кислорода соответственно. Все числа разделены пробелом и не превосходят 1018.
# Выходные данные - В выходной файл OUTPUT.TXT выведите максимально возможное число молекул спирта, которые могут
# получиться из атомов, представленных во входных данных.
c, h, o = map(int, input().split())
print(min(c // 2, h // 6, o))
