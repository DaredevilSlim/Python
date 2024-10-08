#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Карточки - 3
# (Время: 1 сек. Память: 16 Мб Сложность: 22%)
# Студент-первокурсник Антон никак не может понять странную формулу
# 1/2 + 1/3 + 1/4 + ... + 1/n + ... → бесконечность
# Хорошо, что у Антона есть друг Васька, который отлично знает математику. Вот и придумал Васька, как Антошке объяснить
# эту самую бесконечность. Взял колоду карт и стал раскладывать карты на столе. Если есть одна карта, она нависает над
# столом на 1/2 длины карты. Если есть две карты, то верхняя нависает над нижней на 1/2 длины карты, а нижняя - нависает
# над столом на 1/3 длины. В итоге получается нависание 1/2+1/3=5/6. А если у нас есть N карт, то длина нависающей части
# уже 1/2+1/3+1/4+...+1/N.
# И стал Васька с Антоном в такую игру играть: Антон называет какое-нибудь число, а Вася называет минимальное количество
# карт, которое нужно положить, чтобы длина нависающей части была бы не меньше этого числа.
# Напишите программу, которая помогает Васе каждый раз давать правильный ответ.
# Входные данные - Входной файл INPUT.TXT содержит единственное положительное число X - длина нависающей части. Число X
# задано с двумя знаками после запятой и 0.01 ≤ x < 10.00.
# Выходные данные - В выходной файл OUTPUT.TXT выведите ответ на задачу по формату, приведенному в примерах.
a = float(input())
b = 2
while a > 0:
    a -= 1 / b
    b += 1
print(b - 2, 'card(s)')
# Или
a = float(input())
b = 0
c = 2
while a > 0:
    a -= 1 / c
    b += 1
    c += 1
print(b, 'card(s)')
# Или
a = float(input())
b = 0
c = 0
d = 2
while a > b:
    b += 1 / d
    c += 1
    d += 1
print(c, 'card(s)')
