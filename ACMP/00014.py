#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №14 - НОК
# Требуется написать программу, определяющую наименьшее общее кратное (НОК) чисел a и b.
# Входные данные - В единственной строке входного файла INPUT.TXT записаны два натуральных числа А и В через пробел, не
# превышающих 46340.
# Выходные данные - В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — НОК чисел А и В.
a, b = map(int, input().split())
c = a * b
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(c // a)
# Или


def simple(nu, dev=2):
    dev_list = []
    while nu != 1:
        if (nu % dev) == 0:
            dev_list.append(dev)
            nu //= dev
            dev = 2
        else:
            dev += 1
    return dev_list


a, b = input().split()
a, b = simple(int(a)), simple(int(b))
diff = 0
for i in (set(a) & set(b)):
    if a.count(i) > b.count(i):
        diff = a.count(i) - (a.count(i) - b.count(i))
    else:
        diff = a.count(i)
    while diff != 0:
        b.remove(i)
        diff -= 1
nok = 1
for i in (a + b):
    nok *= i
print(nok)
