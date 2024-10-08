#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №844 - Поля
# (Время: 1 сек. Память: 16 Мб Сложность: 16%)
# Геннадий учится в сельской школе и мечтает стать агрономом. На уроке геометрии Геннадий познакомился с новой фигурой –
# прямоугольником. Освоив вычисление площади прямоугольника, Гена подумал о том, что квадратные поля гораздо удобнее,
# нежели прямоугольные. Поразмыслив еще немного, Гена столкнулся с интересной задачей: существует ли такое квадратное
# поле, у которого площадь в точности равна площади заданного поля прямоугольной формы, чтобы при этом длины сторон
# обеих полей были бы целыми числами?
# Входные данные - Входной файл INPUT.TXT содержит целые числа a и b – длины сторон прямоугольника (1 < = a*b ≤ 1014).
# Выходные данные - В выходной файл OUTPUT.TXT выведите либо одно целое число c – длину стороны квадрата, либо 0, если
# квадрата с целочисленной длиной стороны не существует.
a, b = map(int, input().split())
c = a * b
d = int(c ** .5)
print(d if d * d == c else 0)
# Или
a, b = map(float, input().split())
c = int((a * b) ** .5)
print(c if c * c == a * b else 0)
