#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №10 - Уравнение
# (Время: 1 сек. Память: 16 Мб Сложность: 17%)
# Вася в школе изучил квадратные уравнения и понял, как они легко решаются путем вычисления дискриминанта. Но Петя
# поведал ему о методе решения кубических уравнений вида A*X3 + B*X2 + C*X + D = 0. На факультативе по математике Васе
# задали решить около ста уравнений как раз такого вида. Но, к сожалению, Вася забыл формулы, о которых рассказывал ему
# Петя. Но Васе было известно, что все корни уравнений – целые числа и находятся на отрезке [-100, 100]. Поэтому у Васи
# есть шанс найти их методом перебора, но для этого ему придется затратить уйму времени, т.к. возможно необходимо будет
# осуществить перебор нескольких тысяч значений. Помогите Васе написать программу, которая поможет ему найти корни
# кубических уравнений!
# Входные данные - В единственной строке входного файла INPUT.TXT записаны 4 числа: A, B, C и D – целые коэффициенты
# кубического уравнения. Каждый коэффициент по модулю меньше 32768.
# Выходные данные - В единственную строку выходного файла OUTPUT.TXT нужно вывести через пробел в порядке возрастания
# все корни заданного кубического уравнения. Кратные корни следует выводить только один раз.
a, b, c, d = map(int, input().split())
roots = []
for x in range(-100, 101):
    if a * x ** 3 + b * x ** 2 + c * x + d == 0:
        roots.append(x)
print(*roots)
