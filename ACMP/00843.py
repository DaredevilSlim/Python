#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №843 - Экзамены
# (Время: 1 сек. Память: 16 Мб Сложность: 20%)
# В этом году при поступлении в университет абитуриентам требовалось успешно сдать экзамены по математике и физике.
# К сожалению, с этим испытанием справились не все. Известно, что на экзамены пришло N абитуриентов, из них M – сдали
# математику, F – сдали физику, а L – не сдали ни одного предмета. Найдите, сколько абитуриентов сдали оба предмета и
# стали студентами, а также определите, сколько абитуриентов сдали один экзамен: только по математике или только по
# физике.
# Входные данные - Входной файл INPUT.TXT содержит четыре целых числа, разделенных пробелами: N (0 < N ≤ 2×109), M, F,
# L (0 ≤ M, F, L ≤ 2×109).
# Выходные данные - В выходной файл OUTPUT.TXT выведите три числа через пробел:
# a) количество абитуриентов, сдавших оба экзамена;
# b) количество абитуриентов, сдавших только математику;
# с) количество абитуриентов, сдавших только физику.
a, b, c, d = map(int, input().split())
a -= d
print(b + c - a, a - c, a - b)
# Или
a, b, c, d = map(int, input().split())
a -= d
print(abs(a - b - c), a - c, a - b)
