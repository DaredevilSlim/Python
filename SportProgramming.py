#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Перебор всех возможных строк из заданных символов
def sequence(idx=0):
    if idx == a:
        return print(*res)
    for i in range(1, b + 1):
        res[idx] = i
        sequence(idx + 1)


a, b = map(int, input().split())
res = [0] * a
sequence()


# Генерация перестановок
def sequence(idx=0):
    if idx == b:
        return print(*res)
    for i in range(1, b + 1):
        if used[i]:
            continue
        res[idx] = i
        used[i] = True
        sequence(idx + 1)
        used[i] = False


b = int(input())
res = [0] * b
used = [0] * b * b
sequence()


# Правильные скобочные последовательности
def correct(st):
    bal = 0
    for i in range(len(st)):
        if st[i] == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            return False
    return bal


s = input()
print(correct(s))
