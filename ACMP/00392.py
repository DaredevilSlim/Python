#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №392 - Сдвиг перестановки
# (Время: 1 сек. Память: 16 Мб Сложность: 24%)
# Перестановкой порядка n называется последовательность из попарно различных целых положительных чисел p1, p2, ... , pn,
# где каждое 1 ≤ pi ≤ n. Будем говорить, что перестановка q1, q2, ... , qn лексикографически меньше перестановки
# p1, p2, . . . , pn, если существует такое i, что qi < pi, а для любого j < i pj = qj. Циклическим сдвигом на k
# перестановки p1, p2, ... , pn называется последовательность, pk+1, pk+2, ... , pn, p1, ... , pk. Отметим, что любой
# циклический сдвиг перестановки также является перестановкой.
# Ваша задача состоит в том, чтобы найти наименьший лексикографически циклический сдвиг заданной перестановки.
# Входные данные - Первая строка входного файла INPUT.TXT содержит порядок n (1 ≤ n ≤ 105) заданной перестановки. Вторая
# строка содержит числа p1, p2, ... , pn, отделенные друг от друга пробелами.
# Выходные данные - В выходной файл OUTPUT.TXT выведите перестановку, являющуюся наименьшим лексикографически
# циклическим сдвигом перестановки, заданной во входном файле.
a = input()
b = input().split()
c = b.index(min(b))
print(*b[c:], *b[:c])
# Или
a = input()
b = input().split()
c = b.index(min(b))
d = b[c:] + b[:c]
print(*d)
# Или
a = input()
b = list(map(int, input().split()))
c = b.index(min(b))
d = b[c:] + b[:c]
print(*d)
