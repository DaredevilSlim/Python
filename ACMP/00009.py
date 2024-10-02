#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №9 - Домашнее задание
# (Время: 1 сек. Память: 16 Мб Сложность: 27%)
# Петя успевает по математике лучше всех в классе, поэтому учитель задал ему сложное домашнее задание, в котором нужно в
# заданном наборе целых чисел найти сумму всех положительных элементов, затем найти где в заданной последовательности
# находятся максимальный и минимальный элемент и вычислить произведение чисел, расположенных между ними. Так же
# известно, что минимальный и максимальный элемент встречаются в заданном множестве чисел только один раз. Поскольку
# задач такого рода учитель дал Пете около ста, то Петя как сильный программист смог написать программу, которая по
# заданному набору чисел самостоятельно находит решение. А Вам слабо?
# Входные данные - В первой строке входного файла INPUT.TXT записано единственное число N – количество элементов
# массива. Вторая строка содержит N целых чисел, представляющих заданный массив. Все элементы массива разделены
# пробелом. Каждое из чисел во входном файле не превышает 102 по абсолютной величине.
# Выходные данные - В единственную строку выходного файла OUTPUT.TXT нужно вывести два числа, разделенных пробелом:
# сумму положительных элементов и произведение чисел, расположенных между минимальным и максимальным элементами.
# Значения суммы и произведения не превышают по модулю 3*104.
n_count = int(input())
n_list = list(map(int, input().split()))
n_sum, n_mul = 0, 1
for n in n_list:
    if n > 0:
        n_sum += n
n_min, n_max = sorted([n_list.index(min(n_list)), n_list.index(max(n_list))])
for num in n_list[n_min + 1:n_max]:
    n_mul *= num
print(n_sum, n_mul)
