#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №86 - Головоломка про ферзей
# (Время: 1 сек. Память: 16 Мб Сложность: 15%)
# Вероятно, что многие из вас играли в шахматы. Поэтому вы знаете, что ферзь может двигаться по горизонталям, вертикалям
# и диагоналям.
# Вася недавно начал заниматься шахматами и где-то прочел головоломку, в которой нужно было расставить максимальное
# количество ферзей на доске 8х8 так, чтобы хотя бы одно поле оказалось небитым. Эта задача легко решается для доски
# 3х3, т.к. понятно, что более двух ферзей расставить таким образом на ней невозможно.
# Помогите Васе решить эту задачу для доски N×N.
# Входные данные - В единственной строке входного файла INPUT.TXT записано натуральное число N – размеры шахматной доски
# N×N (1 ≤ N ≤ 100).
# Выходные данные - В единственную строку выходного файла OUTPUT.TXT нужно вывести максимальное количество ферзей,
# которых можно расставить на шахматной доске N×N так, чтобы одна клетка оставалась небитой.
n = int(input())
print(n * n - 3 * n + 2)
# Или
n = int(input())
print((n - 1) * (n - 2))
