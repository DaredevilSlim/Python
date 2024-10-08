#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Карусель
# (Время: 1 сек. Память: 16 Мб Сложность: 22%)
# Карусель – одна из популярных форм проведения командных соревнований по решению задач. Наибольшую известность в
# использовании данной модели в России получил ресурс «Интернет-карусели», расположенный в сети Интернет по адресу
# http://karusel.desc.ru.
# Всем командам, участвующим в карусели, предлагаются в строгом порядке одни и те же задачи, которые необходимо решить в
# установленное время. Система подсчета баллов такова, что доминирующим фактором является не количество решенных задач,
# а длины последовательностей правильных решений.
# Начисление баллов происходит согласно следующей схеме:
# первая задача стоит 3 балла;
# если к задаче дан верный ответ, то команда получает ее стоимость, а следующая задача будет стоить на 1 балл больше;
# если на задачу дан неверный ответ, то команда получает за решение 0 баллов, а следующая задача будет стоить на 3 балла
# меньше, но не менее 3 баллов.
# Вам требуется написать программу, которая по результатам ответов команды определит итоговый балл.
# Входные данные - Первая строка входного файла INPUT.TXT содержит натуральное число N – количество задач в карусели
# (N ≤ 105). Во второй строке расположены N цифр 0 или 1, разделенные пробелом; i-я цифра соответствует корректности
# ответа команды на i-ю задачу (0 – неверный ответ, 1 – верный ответ).
# Выходные данные - В выходной файл OUTPUT.TXT выведите целое число – количество набранных баллов.
a = input()
c = 3
d = 0
for i in map(int, input().split()):
    if i > 0:
        d += c
        c += 1
    else:
        c = c - 3 if c > 5 else 3
print(d)
# Или
a = int(input())
b = list(map(int, input().split()))
c = 3
d = 0
for i in range(a):
    if b[i] > 0:
        d += c
        c += 1
    else:
        c = c - 3 if c > 5 else 3
print(d)
# Или
a = int(input())
b = list(map(int, input().split()))
c = 3
for i in range(a):
    if b[i] == 1:
        b[i] = c
        c += 1
    elif b[i] == 0:
        b[i] = 0
        if c - 3 >= 3:
            c -= 3
        else:
            c = 3
print(sum(b))

