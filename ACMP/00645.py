#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №645 - Красивая стена
# (Время: 1 сек. Память: 16 Мб Сложность: 25%)
# Однажды великий художник Гигабайт подарил королю Байтландии одно из своих лучших полотен. Король, впечатленный
# произведением Гигабайта, в знак благодарности подарил ему K плиток из очень ценной разновидности мрамора размером
# 10×10 сантиметров каждая.
# Художник решил украсить этими плитками одну из стен своего дома. Он задумал выложить из них прямоугольник высотой H
# плиток и шириной W плиток. Художник понимает, что число вариантов для выбора H и W достаточно велико. Из всех
# возможных вариантов он хочет выбрать самый красивый. Ваша задача – помочь ему с выбором!
# Для определения степени красоты художник решил учитывать два параметра:
# Насколько выбранный прямоугольник будет близок к квадрату. Значение этого параметра равно модулю разности чисел H и
# W(т.е. |H-W|).
# Сколько плиток останется невостребованными после украшения стены. Значение этого параметра равно разности чисел K и
# H×W(т.е. K-H×W, где K ≥ H×W ).
# Степень красоты вычисляется как сумма значений двух описанных выше параметров. Например, имея 11 плиток, можно выбрать
# прямоугольник 3×3, степень красоты равна 0+2 = 2. Также можно выбрать прямоугольник 2×5, тогда степень красоты равна
# 3+1 = 4. Считается, что чем меньше степень красоты, тем красивее прямоугольник.
# Ваша задача – написать программу, которая по заданному числу K находит размеры самого красивого прямоугольника.
# Входные данные - Единственная строка входного файла INPUT.TXT содержит одно целое число K – количество подаренных
# королем плиток (1 ≤ K ≤ 10^6).
# Выходные данные - Единственная строка выходного файла OUTPUT.TXT должна содержать натуральные числа H и W
# соответственно, которые определяют размеры самого красивого прямоугольника. Числа должны быть разделены одиночным
# пробелом. Если решений несколько, выведите любое из них.
a = int(input())
b = a
c = ''
for i in range(1, a + 1):
    d = a // i
    e = abs(a - d * i) + abs(d - i)
    if e < b:
        b = e
        c = f'{i} {d}'
print(c)
