#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №274 - Дружные числа
# (Время: 1 сек. Память: 16 Мб Сложность: 25%)
# Будем называть два числа дружными, если они состоят из одних и тех же цифр. Например, числа 1132 и 32321 являются
# дружными, а 12 и 123 – нет (в первом числе нет цифры 3). Требуется написать программу, которая определит, являются ли
# два заданных числа дружными.
# Входные данные - Входной текстовый файл INPUT.TXT содержит в первой строке натуральное число K – количество тестов.
# Количество тестов не превышает 10. В следующих K строках содержатся по два целых числа A и B, разделенные одним
# пробелом (0 < A < 109, 0 < B < 109).
# Выходные данные - Выходной текстовый файл OUTPUT.TXT должен содержать K строк. Для каждого теста в отдельной строке
# надо выдать сообщение “YES”, если A и B являются дружными, или “NO”, если не являются. В сообщениях кавычки не
# печатать.
for _ in ' ' * int(input()):
    a, b = map(set, input().split())
    print('YES' if a == b else 'NO')