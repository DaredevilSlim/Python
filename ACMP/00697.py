#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# ЗАДАЧА №697 - Ремонт
# (Время: 1 сек. Память: 16 Мб Сложность: 11%)
# Ваш любимый дядя – директор фирмы, которая делает евроремонты в офисах. В связи с финансово-экономическим кризисом,
# дядюшка решил оптимизировать свое предприятие.
# Давно ходят слухи, что бригадир в дядюшкиной фирме покупает лишнее количество стройматериалов, а остатки использует
# для отделки своей новой дачи. Ваш дядя заинтересовался, сколько в действительности банок краски необходимо для
# покраски стен в офисе длиной L метров, шириной – W и высотой – H, если одной банки хватает на 16м2, а размерами дверей
# и окон можно пренебречь? Заказов много, поэтому дядя попросил написать программу, которая будет все это считать.
# Входные данные - Входной файл INPUT.TXT содержит три натуральных числа L, W, H – длину, ширину и высоту офиса в метрах
# соответственно, каждое из которых не превышает 1000.
# Выходные данные - В выходной файл OUTPUT.TXT выведите одно целое число – минимальное количество банок краски,
# необходимых для покраски стен в офисе.
l, w, h = map(int, input().split())
print(math.ceil(2 * (l + w) * h / 16))
