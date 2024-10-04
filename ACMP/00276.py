#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №276 - Разбиение на части
# (Время: 1 сек. Память: 16 Мб Сложность: 21%)
# Необходимо представить целое число N в виде суммы M примерно равных целых чисел. Будем считать, что числа примерно
# равны, если они отличаются друг от друга не более чем на единицу.
# Входные данные - Во входном файле INPUT.TXT записаны два натуральных числа N и M через пробел, каждое из которых не
# превосходит 30000.
# Выходные данные - Выходной файл OUTPUT.TXT должен содержать M примерно равных целых чисел, сумма которых должна быть
# равна N. Все числа следует вывести в одной строке в порядке неубывания через пробел.
a, b = map(int, input().split())
c = a // b
a -= c * b
print(*[c] * (b - a) + [c + 1] * a)
# Или
a, b = map(int, input().split())
c = a // b
a -= c * b
e = [c] * (b - a) + [c + 1] * a
print(*e)
# Или
a, b = map(int, input().split())
c = a // b
d = a - c * b
e = [c + 0] * (b - d) + [c + 1] * d
print(*e)
# Или
a, b = map(int, input().split())
c = a // b
d = a % b
e = a - c * b
f = b - e
g = b - f
h = [0] * f + [1] * g
for i in range(b):
    print(h[i] + c, end=' ')
