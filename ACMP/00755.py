#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №755 - Сбор земляники
# (Время: 1 сек. Память: 16 Мб Сложность: 6%)
# Маша и Миша собирали землянику. Маше удалось сорвать X ягод, а Мише – Y ягод. Поскольку ягода была очень вкусной, то
# ребята могли какую то часть ягод съесть. По нашим подсчетам вместе они съели Z ягод.
# Требуется определить: сколько ягод ребята собрали в результате, при этом следует проверить, не ошиблись ли мы в
# расчетах, подсчитывая количество съеденных ягод (их не должно было получиться больше, чем сорванных ягод).
# Входные данные - Входной файл INPUT.TXT содержит три натуральных числа X, Y и Z, не превышающих 1000. Все числа
# расположены в первой строке файла и разделены пробелом.
# Выходные данные - В выходной файл OUTPUT.TXT выведите количество собранных ягод, если наши подсчеты оказались
# правдоподобными, либо слово «Impossible» в противном случае.
x, y, z = map(int, input().split())
print('Impossible' if x + y < z else x + y - z)
# Или
x, y, z = map(int, input().split())
print(x + y - z if x + y >= z else 'Impossible')