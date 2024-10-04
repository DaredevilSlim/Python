#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №7	- Золото племени АББА
# (Время: 1 сек. Память: 16 Мб Сложность: 30%)
# Главный вождь племени Абба не умеет считать. В обмен на одну из его земель вождь другого племени предложил ему выбрать
# одну из трех куч с золотыми монетами. Но вождю племени Абба хочется получить наибольшее количество золотых монет.
# Помогите вождю сделать правильный выбор!
# Входные данные - В первой строке входного файла INPUT.TXT записаны три натуральных числа через пробел. Каждое из чисел
# не превышает 10100. Числа записаны без ведущих нулей.
# Выходные данные - В выходной файл OUTPUT.TXT нужно вывести одно целое число — максимальное количество монет, которые
# может взять вождь.
print(max(map(int, input().split())))
# Или
heap = map(int, input().split())
print(max(heap))
