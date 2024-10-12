#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №819 - Прямоугольный параллелепипед
# (Время: 1 сек. Память: 16 Мб Сложность: 10%)
# Прямоугольный параллелепипед - это объемная фигура, у которой шесть граней, и каждая из них является прямоугольником.
# Моделями прямоугольного параллелепипеда служат классная комната, кирпич, спичечная коробка. Длины трех ребер
# прямоугольного параллелепипеда, имеющих общий конец, называют его измерениями. На приведенном рисунке измерения
# представлены ребрами AB, BC и BF с общим концом в точке B, а значения измерений равны их длинам a, b и c
# соответственно.
# По заданным измерениям прямоугольного параллелепипеда Вам необходимо определить площадь его поверхности и объем.
# Входные данные - Единственная строка входного файла INPUT.TXT содержит разделенные пробелом три натуральных числа A, B
# и С – измерения параллелепипеда, каждое из измерений не превышает 106.
# Выходные данные - В выходной файл OUTPUT.TXT выведите через пробел два целых числа: площадь поверхности и объем
# заданного параллелепипеда.
a, b, c = map(int, input().split())
print(2 * (a * b + b * c + a * c), a * b * c)
# Или
a, b, c = map(int, input().split())
print(a * b * 2 + b * c * 2 + a * c * 2, a * b * c)