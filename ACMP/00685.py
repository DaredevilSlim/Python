#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №685 - Золотой песок
# (Время: 1 сек. Память: 16 Мб Сложность: 10%)
# Сотрудники завода по производству золотого песка из воздуха решили поправить свое финансовое положение. Они пробрались
# на склад завода, где хранился золотой песок трех видов. Один килограмм золотого песка первого вида они смогли бы
# продать за A1 рублей, второго вида – за A2 рублей, а третьего вида – за A3 рублей. Так получилось, что у сотрудников
# оказалось с собой только три емкости: первая была рассчитана на B1 килограмм груза, вторая на B2 килограмм, а третья
# на B3 килограмм. Им надо было заполнить полностью все емкости таким образом, чтобы получить как можно больше денег за
# весь песок. При заполнении емкостей нельзя смешивать песок разных видов, то есть, в одну емкость помещать более одного
# вида песка, и заполнять емкости песком так, чтобы один вид песка находился более чем в одной емкости.
# Требуется написать программу, которая определяет, за какую сумму предприимчивые сотрудники смогут продать весь песок в
# случае наилучшего для себя заполнения емкостей песком.
# Входные данные - В единственной строке входного файла INPUT.TXT записано 6 натуральных чисел A1, A2, A3, B1, B2, B3,
# записанных в одной строке через пробел. Все числа не превосходят 100.
# Выходные данные - В единственную строку выходного файла OUTPUT.TXT нужно вывести единственное целое число – сумму в
# рублях, которую смогут сотрудники заработать в случае наилучшего для себя заполнения емкостей песком.
g = [int(i) for i in input().split()]
a, b, c = sorted(g[:3])
d, e, f = sorted(g[3:])
print(a * d + b * e + c * f)
# Или
g = list(map(int, input().split()))
a, b, c = sorted(g[:3])
d, e, f = sorted(g[3:])
print(a * d + b * e + c * f)
# Или
g = list(map(int, input().split()))
f = sorted(g[:3])
s = sorted(g[3:])
print(f[0] * s[0] + f[1] * s[1] + f[2] * s[2])
