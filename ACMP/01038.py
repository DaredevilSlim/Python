#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №1038 - Перевязь
# (Время: 1 сек. Память: 16 Мб Сложность: 12%)
# Портос хочет украсить золотым шитьем свою перевязь. Он знает, что один сантиметр золотого шитья стоит один луидор.
# Портосу надо вышить N миллиметров перевязи. Причем мастер никогда не возьмется за работу, если ему заплатят меньше,
# чем стоит работа. И сдачу мастер никогда не отдает.
# Какое минимальное количество луидоров Портос должен заплатить мастеру за работу?
# Входные данные - Входной файл INPUT.TXT содержит натуральное число N (N ≤ 109) – длина перевязи в миллиметрах.
# Выходные данные - В выходной файл OUTPUT.TXT выведите минимальное количество луидоров, которые Портос должен отдать за
# работу.
a = int(input())
b = a // 10
print(b + 1 if a % 10 else b)
# Или
a, b = str(int(input()) / 10).split('.')
print(int(a) + 1 if int(b) else a)

