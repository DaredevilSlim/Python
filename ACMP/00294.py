#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №294 - Болты и гайки
# (Время: 1 сек. Память: 16 Мб Сложность: 17%)
# Вновь созданная фирма купила заброшенные склады на окраине города. Новому заведующему складами поручили произвести
# учёт в короткие сроки. Всё шло хорошо, пока случайно не рассыпали контейнеры с болтами и гайками на каждом складе,
# после чего собрали их в общие (для болтов и гаек) контейнеры, потеряв при этом несколько деталей.
# Помогите оценить нанесённый ущерб на каждом складе, приняв во внимание, что, помимо потерянных деталей, болт (или
# гайка) считается непригодным, если он не имеет соответствующей гайки (или болта).
# Входные данные - Во входном файле INPUT.TXT описано текущее положение на складе. В первой строке через пробел записаны
# три целых числа: k1, l1, m1 – начальное число болтов (100 ≤ k1 ≤ 30000, k1 кратно 100), процент потерянных деталей (0
# ≤ l1 ≤ 100) и стоимость одного болта (1 ≤ m1 ≤ 100) соответственно. Во второй строке через пробел записаны также три
# целых числа: k2, l2, m2 – начальное число гаек (100 ≤ k2 ≤ 30000, k2 кратно 100), процент потерянных деталей (0 ≤ l2 ≤
# 100) и стоимость одной гайки (1 ≤ m2 ≤ 100) соответственно.
# Выходные данные - В выходной OUTPUT.TXT выведите одно целое число – размер ущерба.
a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
b *= a // 100
e *= d // 100
a -= b + d - e
print(b * c + e * f + a * (c if a > 0 else -f))
# Или
a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
b *= a // 100
e *= d // 100
a -= b + d - e
print(b * c + e * f + abs(a) * c if a > 0 else f)
# Или
a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
g = a * b // 100
h = d * e // 100
a -= g
d -= h
print(g * c + h * f + abs(a - d) * (c if a > d else f))
# Или
a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
g = a * b // 100
h = d * e // 100
a -= g
d -= h
print(g * c + h * f + ((a - d) * c if a > d else (d - a) * f))
