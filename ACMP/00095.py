#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №95 - Нумеролог
# (Время: 1 сек. Память: 16 Мб Сложность: 24%)
# Чтобы предсказать судьбу человека, нумеролог берет время жизни человека в секундах, затем складывает все цифры этого
# числа. Если полученное число состоит более чем из одной цифры, операция повторяется, пока в числе не останется одна
# цифра. Затем по полученной цифре и числу операций, необходимых для преобразования числа в цифру нумеролог
# предсказывает судьбу человека. Нумеролог плохо умеет считать, а числа, с которыми он работает, могут быть очень
# большими. Напишите программу, которая бы делала все расчеты за него.
# Входные данные - Входной файл INPUT.TXT содержит число N – время жизни человека в секундах (1 ≤ N ≤ 101000).
# Выходные данные - В выходной файл OUTPUT.TXT выведите два числа через пробел: полученную цифру из числа N и число
# преобразований.
a = input()
b = 0
while len(a) > 1:
    a = str(sum(int(i) for i in a))
    b += 1
print(a, b)
