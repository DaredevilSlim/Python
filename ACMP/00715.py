#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №715 - Миша и негатив
# (Время: 1 сек. Память: 16 Мб Сложность: 17%)
# Миша уже научился хорошо фотографировать и недавно увлекся программированием. Первая программа, которую он написал,
# позволяет формировать негатив бинарного черно-белого изображения.
# Бинарное черно-белое изображение – это прямоугольник, состоящий из пикселей, каждый из которых может быть либо
# черным, либо белым. Негатив такого изображения получается путем замены каждого черного пикселя на белый, а каждого
# белого пикселя – на черный.
# Миша, как начинающий программист, написал свою программу с ошибкой, поэтому в результате ее исполнения мог получаться
# некорректный негатив. Для того чтобы оценить уровень несоответствия получаемого негатива исходному изображению, Миша
# начал тестировать свою программу.
# В качестве входных данных он использовал исходные изображения. Сформированные программой негативы он начал тщательно
# анализировать, каждый раз определяя число пикселей негатива, которые получены с ошибкой.
# Требуется написать программу, которая в качестве входных данных использует исходное бинарное черно-белое изображение
# и полученный Мишиной программой негатив, и на основе этого определяет количество пикселей, в которых допущена ошибка.
# Входные данные - Первая строка входного файла INPUT.TXT содержит целые числа n и m (1 ≤ n, m ≤ 100) – высоту и ширину
# исходного изображения (в пикселях). Последующие n строк содержат описание исходного изображения. Каждая строка
# состоит из m символов «B» и «W». Символ «B» соответствует черному пикселю, а символ «W» – белому. Далее следует
# пустая строка, а после нее – описание выведенного Мишиной программой изображения в том же формате, что и исходное
# изображение.
# Выходные данные - В выходной файл OUTPUT.TXT необходимо вывести число пикселей негатива, которые неправильно
# сформированы Мишиной программой.
n = int(input().split()[0])
a = ''
b = ''
d = 0
for _ in ' ' * n:
    a += input()
c = input()
for _ in ' ' * n:
    b += input()
for i, j in zip(a, b):
    if i == j:
        d += 1
print(d)
# Или
n = int(input().split()[0])
a = ''
b = ''
d = 0
for i in range(n):
    a += input()
c = input()
for i in range(n):
    b += input()
for i, j in zip(a, b):
    if i == j:
        d += 1
print(d)
# Или
n, m = map(int, input().split())
a = ''
b = ''
d = 0
for i in range(n):
    a += input()
c = input()
for i in range(n):
    b += input()
for i, j in zip(a, b):
    if i == j:
        d += 1
print(d)
