#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Существует четыре миссии связанные с анализом частей строки. Все они были созданы за один день и не требуют более
# одного дня для своего решения. Эти миссии можно с легкостью преодолеть посредством простого перебора символов. Но,
# возможно, есть вариант получше? (У Вас может еще не быть доступа ко всем этим миссиям, но по мере открытия островов на
# карте он будет предоставлен)
# Это первая миссия из серии. Вам необходимо найти длину самой длинной подстроки, которая состоит из одинаковых букв.
# Например, строка 'aaabbcaaaa' состоит из четырех подстрок с одинаковыми буквами 'aaa', 'bb','c' и 'aaaa'. Последняя
# подстрока является самой длинной, что и делает ее ответом.
# Входные данные: Строка.
# Выходные данные: Целое число.
def long_repeat(line: str) -> int:
    """
    length the longest substring that consists of the same char
    """
    if not line:
        return 0
    if len(line) == 1:
        return 1
    a = 0
    l = []
    for i in range(len(line) - 1):
        l.append(0)
        l[a] += 1
        if line[i] == line[i+1]:
            if i+1 == len(line) - 1:
                l[a-1] += 1
        else:
            a += 1
    return max(l)


print(long_repeat('sdsffffse'))     # 4
print(long_repeat('ddvvrwwwrggg'))  # 3
print(long_repeat(''))              # 0
print(long_repeat('aa'))            # 2
print(long_repeat('abababaab'))     # 2
print(long_repeat('abababa'))       # 1
print(long_repeat('a'))             # 1

