#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №327 - В одном шаге от счастья
# (Время: 1 сек. Память: 16 Мб Сложность: 16%)
# Вова купил билет в трамвае 13-го маршрута и сразу посчитал суммы первых трёх цифр и последних трёх цифр номера билета
# (номер у билета шестизначный). Оказалось, что суммы отличаются ровно на единицу. «Я в одном шаге от счастья», —
# подумал Вова, — «или предыдущий или следующий билет точно счастливый». Прав ли он?
# Входные данные - Входной файл INPUT.TXT содержит в первой строке число K – количество тестов. В следующих K строках
# записаны номера билетов. Количество тестов не больше 10. Номер состоит ровно из шести цифр, среди которых могут быть и
# нули. Гарантируется, что Вова умеет считать, то есть суммы первых трех цифр и последних трех цифр отличаются ровно на
# единицу.
# Выходные данные - Выходной файл OUTPUT.TXT должен содержать K строк, в каждой из которых для соответствующего теста
# следует указать "Yes", если Вова прав, и "No", если нет.
for _ in ' ' * int(input()):
    n = [int(i) for i in input()]
    f = sum(n[:3])
    x = n[3] + n[4]
    s = x + (n[5] + 1) % 10
    k = x + (n[5] - 1) % 10
    print('Yes' if f == k or f == s else 'No')
# Или
for _ in ' ' * int(input()):
    n = [int(i) for i in input()]
    f = sum(n[:3])
    s = n[3] + n[4] + (n[5] + 1) % 10
    k = n[3] + n[4] + (n[5] - 1) % 10
    print('Yes' if f == k or f == s else 'No')
