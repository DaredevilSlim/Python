#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №387 - Левая рекурсия
# (Время: 1 сек. Память: 16 Мб Сложность: 20%)
# В теории формальных грамматик и автоматов (ТФГиА) важную роль играют так называемые контекстно-свободные грамматики
# (КС-грамматики). КС-грамматикой будем называть четверку, состоящую из множества N нетерминальных символов, множества T
# терминальных символов, множества P правил (продукций) и начального символа S, принадлежащего множеству N.
# Каждая продукция p из P имеет форму A –> a, где A нетерминальный символ (A из N), а a – строка, состоящая из
# терминальных и нетерминальных символов. Процесс вывода слова начинается со строки, содержащей только начальный символ
# S. После этого на каждом шаге один из нетерминальных символов, входящих в текущую строку, заменяется на правую часть
# одной из продукций, в которой он является левой частью. Если после такой операции получается строка, содержащая только
# терминальные символы, то процесс вывода заканчивается.
# Во многих теоретических задачах удобно рассматривать так называемые нормальные формы грамматик. Процесс приведения
# грамматики к нормальной форме часто начинается с устранения левой рекурсии. В этой задаче мы будем рассматривать
# только ее частный случай, называемый непосредственной левой рекурсией. Говорят, что правило вывода A –> R содержит
# непосредственную левую рекурсию, если первым символом строки R является A.
# Задана КС-грамматика. Требуется найти количество правил, содержащих непосредственную левую рекурсию.
# Входные данные - Первая строка входного файла INPUT.TXT содержит количество n (1 ≤ n ≤ 1000) правил в грамматике.
# Каждая из последующих n строк содержит по одному правилу. Нетерминальные символы обозначаются заглавными буквами
# английского алфавита, терминальные - строчными. Левая часть продукции отделяется от правой символами –>. Правая часть
# продукции имеет длину от 1 до 30 символов.
# Выходные данные - В выходной файл OUTPUT.TXT выведите ответ на задачу.
c = 0
for _ in ' ' * int(input()):
    r = input()
    if r[0] == r[3]:
        c += 1
print(c)
# Или
c = 0
for i in range(int(input())):
    r = input()
    if r[0] == r[3]:
        c += 1
print(c)
