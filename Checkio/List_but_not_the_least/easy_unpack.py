#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ваша цель сейчас — создать функцию, которая принимает на вход кортеж и возвращает кортеж из 3 элементов: первого,
# третьего и второго с конца элементов заданного кортежа.
# Важно отметить, что вам нужно использовать индекс для извлечения элементов из кортежа. Обратите внимание, нумерация
# индексов начинается с 0, не с 1. Это означает, что если вы хотите получить первый элемент из кортежа elements, вам
# нужен elements[0], а если второй — elements[1].
# Входные данные: Кортеж длиной не менее 3 элементов.
# Выходные данные: Кортеж.
def easy_unpack(elements: tuple) -> tuple:
    return elements[0], elements[2], elements[-2]


print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))  # (1, 3, 7)
print(easy_unpack((1, 1, 1, 1)))              # (1, 1, 1)
print(easy_unpack((6, 3, 7)))                 # (6, 7, 3)
