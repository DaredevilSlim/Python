#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №693 - Перестановка
# (Время: 1 сек. Память: 16 Мб Сложность: 24%)
# Если Вы читали Гарри Поттера, то знаете, что повелитель зла, Лорд Волдеморт создал свое имя путем перестановки букв в
# своем настоящем имени. Так из имени «Tom Marvolo Riddle» он получил «I am Lord Voldemort».
# Напишите программу, которая проверяет, можно ли получить из одного имени другое путем перестановки его букв. При этом
# регистром букв нужно пренебречь.
# Входные данные - В первой строке входного файла INPUT.TXT записаны два слова, разделенные единственным в строке
# пробелом. Слова содержат только символы английского алфавита. Длина слов больше 0 и не превышает 50 символов.
# Выходные данные - В выходной файл OUTPUT.TXT выведите «Yes», если возможно получить из одного имени другое, и «No» в
# противном случае.
a, b = map(sorted, input().lower().split())
print(a == b and 'Yes' or 'No')
# Или
a, b = map(sorted, input().lower().split())
print('Yes' if a == b else 'No')
# Или
a, b = input().lower().split()
print('Yes' if sorted(a) == sorted(b) else 'No')
# Или
a, b = map(str.lower, input().split())
print('Yes' if sorted(a) == sorted(b) else 'No')
# Или
a, b = map(str.lower, input().split())
print('Yes' if sorted(i for i in a) == sorted(j for j in b) else 'No')
# Или
a, b = input().split()
print('Yes' if sorted(i.lower() for i in a) == sorted(j.lower() for j in b) else 'No')
# Или
a, b = input().split()
a = sorted(i.lower() for i in a)
b = sorted(j.lower() for j in b)
print('Yes' if a == b else 'No')
