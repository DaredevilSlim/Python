#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №694 - Лентяй
# (Время: 1 сек. Память: 16 Мб Сложность: 21%)
# Студент Валера являет собой классический пример лентяя. На занятия он практически не ходит, и только в конце семестра
# появляется в университете и сдает ”хвосты”. Его заветная мечта: найти такой день, когда можно будет сдать сразу все
# долги. У него есть расписание работы преподавателей, из которого точно известно, с какого и по какой день месяца
# каждый преподаватель ежедневно будет доступен.
# Помогите Валере написать программу, которая по расписанию будет определять, сможет ли Валера сдать все долги за один
# день или нет.
# Входные данные - В первой строке входного файла INPUT.TXT содержится натуральное число N – количество предметов,
# которые нужно сдать Валере (N ≤ 100). Далее идет N строк, каждая из которых состоит из двух чисел A и B, задающих
# отрезок работы очередного преподавателя (1 ≤ A ≤ B ≤ 31).
# Выходные данные - В выходной файл OUTPUT.TXT выведите «YES», если возможно встретить всех преподавателей за один день,
# или «NO», если это сделать невозможно.
b = []
for _ in ' ' * int(input()):
    *a, = map(int, input().split())
    b.append(list(range(a[0], a[1] + 1)))
c = [0] * len(b[0])
for i in range(1, len(b)):
    for j in range(len(b[0])):
        if b[0][j] in b[i]:
            c[j] += 1
print('YES' if (len(b) - 1) in c else 'NO')