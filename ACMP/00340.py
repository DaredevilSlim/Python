#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №340 - Коробки
# (Время: 1 сек. Память: 16 Мб Сложность: 19%)
# На столе лежат коробка размера A1 × B1 × C1 и коробка размера A2 × B2 × C2. Выясните можно ли одну из этих коробок
# положить в другую, если разрешены повороты коробок вокруг любого ребра на угол 90 градусов.
# Входные данные - Первая строка входного файла содержит три целых числа A1, B1 и C1. Вторая строка входного файла
# содержит три целых числа A2, B2 и C2. Все числа положительны и не превосходят 1000.
# Выходные данные - Если коробки одинаковы, выведите "Boxes are equal". Если первая коробка может быть положена во
# вторую, выведите "The first box is smaller than the second one". Если вторая коробка может быть положена в первую,
# выведите "The first box is larger than the second one". Иначе, выведите "Boxes are incomparable".
a, b, c = sorted(map(int, input().split()))
d, e, f = sorted(map(int, input().split()))
g = 'Boxes are '
h = 'The first box is %s than the second one'
print(g + 'equal'
      if a == d and b == e and c == f
      else h % 'larger'
      if a >= d and b >= e and c >= f
      else h % 'smaller'
      if a <= d and b <= e and c <= f
      else g + 'incomparable')
# Или
a, b, c = sorted(map(int, input().split()))
d, e, f = sorted(map(int, input().split()))
print('Boxes are equal'
      if a == d and b == e and c == f
      else 'The first box is larger than the second one'
      if a >= d and b >= e and c >= f
      else 'The first box is smaller than the second one'
      if a <= d and b <= e and c <= f
      else 'Boxes are incomparable')
# Или
a1, b1, c1 = sorted(map(int, input().split()))
a2, b2, c2 = sorted(map(int, input().split()))
if a1 == a2:
    if b1 == b2:
        if c1 == c2:
            print('Boxes are equal')
        elif c1 > c2:
            print('The first box is larger than the second one')
        elif c1 < c2:
            print('The first box is smaller than the second one')
    elif b1 > b2:
        if c1 == c2:
            print('The first box is larger than the second one')
        elif c1 > c2:
            print('The first box is larger than the second one')
        else:
            print('Boxes are incomparable')
    elif b1 < b2:
        if c1 == c2:
            print('The first box is smaller than the second one')
        elif c1 < c2:
            print('The first box is smaller than the second one')
        else:
            print('Boxes are incomparable')
elif a1 > a2:
    if b1 == b2:
        if c1 == c2:
            print('The first box is larger than the second one')
        elif c1 > c2:
            print('The first box is larger than the second one')
        else:
            print('Boxes are incomparable')
    elif b1 > b2:
        if c1 == c2:
            print('The first box is larger than the second one')
        elif c1 > c2:
            print('The first box is larger than the second one')
        else:
            print('Boxes are incomparable')
    else:
        print('Boxes are incomparable')
elif a1 < a2:
    if b1 == b2:
        if c1 == c2:
            print('The first box is smaller than the second one')
        elif c1 < c2:
            print('The first box is smaller than the second one')
        else:
            print('Boxes are incomparable')
    elif b1 < b2:
        if c1 == c2:
            print('The first box is smaller than the second one')
        elif c1 < c2:
            print('The first box is smaller than the second one')
        else:
            print('Boxes are incomparable')
    else:
        print('Boxes are incomparable')
else:
    print('Boxes are incomparable')
