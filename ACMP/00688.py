#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №688 - Суслик и собака
# (Время: 1 сек. Память: 16 Мб Сложность: 19%)
# На большом поле находятся суслик и собака. Собака хочет суслика съесть, а суслик хочет оказаться в безопасности,
# добежав до одной из норок, выкопанных в поле. Ни собака, ни суслик в математике не сильны, но, с другой стороны, они и
# не беспросветно глупы. Суслик выбирает определенную норку и бежит к ней по прямой с определенной скоростью. Собака,
# которая очень хорошо понимает язык телодвижений, угадывает, к какой норке бежит суслик, и устремляется к ней со
# скоростью вдвое большей скорости суслика. Если собака добегает до норки первой (раньше суслика), то она съедает
# суслика; иначе суслик спасается.
# Требуется написать программу, которая поможет суслику выбрать норку, в которой он может спастись, если таковая
# существует.
# Входные данные - Во входном файле INPUT.TXT записано в первой строке два числа – координаты суслика. Во второй строке
# записаны два числа – координаты собаки. В третьей строке записано число n – число норок на поле. В следующих n строках
# записаны координаты норок. Все координаты являются целыми числами, по модулю не превышающими 10000, и записываются
# через пробел. Количество норок не превышает 1000.
# Выходные данные - В единственную строку выходного файла OUTPUT.TXT нужно вывести число – номер норки, если у суслика
# есть возможность в ней спастись. Если у суслика есть возможность спрятаться в нескольких норках, то выведите ту,
# которая первая шла во входных данных. Если суслик не может спастись, то выведите в выходной файл «NO» (без кавычек).
g = []
a, b = map(int, input().split())
c, d = map(int, input().split())
for i in range(int(input())):
    e, f = map(int, input().split())
    if ((a - e) ** 2 + (b - f) ** 2) ** .5 <= (((c - e) ** 2 + (d - f) ** 2) ** .5) / 2:
        g.append(i + 1)
print(g[0] if len(g) > 0 else 'NO')
# Или
g = []
a, b = map(int, input().split())
c, d = map(int, input().split())
for i in range(1, int(input()) + 1):
    e, f = map(int, input().split())
    h = ((a - e) ** 2 + (b - f) ** 2) ** 0.5
    j = (((c - e) ** 2 + (d - f) ** 2) ** 0.5) / 2
    if h <= j:
        g.append(i)
print(g[0] if len(g) > 0 else 'NO')