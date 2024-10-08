#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №892 - Время года
# (Время: 1 сек. Память: 16 Мб Сложность: 10%)
# По заданному номеру месяца в году требуется определить время года.
# Входные данные - Входной файл INPUT.TXT содержит натуральное число N (N≤100) – номер месяца.
# Выходные данные - В выходной файл OUTPUT.TXT выведите для летних месяцев значение «Summer», для зимних – «Winter», для
# весенних – «Spring», для осенних – «Autumn». Если число не соответствует возможному значению месяца, то в этом случае
# следует вывести «Error».
m = input()
print('Winter' if m in '12'
      else 'Spring' if m in '345' else 'Summer' if m in '678' else 'Autumn' if m in '91011' else 'Error')
