#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from timeit import Timer


def summa_one(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


def summa_two(n):
    summa = (n * (n + 1)) / 2
    return summa


t = Timer('summa_one(10000)', 'from __main__ import summa_one')
print('{0:.6f}'.format(t.timeit(number=1)))

t = Timer('summa_one(100000)', 'from __main__ import summa_one')
print('{0:.6f}'.format(t.timeit(number=1)))

t = Timer('summa_one(1000000)', 'from __main__ import summa_one')
print('{0:.6f}'.format(t.timeit(number=1)))


t = Timer('summa_two(10000)', 'from __main__ import summa_two')
print('{0:.6f}'.format(t.timeit(number=1)))

t = Timer('summa_two(100000)', 'from __main__ import summa_two')
print('{0:.6f}'.format(t.timeit(number=1)))

t = Timer('summa_two(1000000)', 'from __main__ import summa_two')
print('{0:.6f}'.format(t.timeit(number=1)))


def anagrama_one(s_one: str, s_two: str)->bool:
    if sorted(s_one) != sorted(s_two):
        return False
    return True


t = Timer('anagrama_one("а роза упала на лапу азора", "а роза упала на лапу азора")',
          'from __main__ import anagrama_one')
print('{0:.6f}'.format(t.timeit(number=1)))

print(anagrama_one("а роза упала на лапу азора", "а роза упала на лапу азора"))
print(anagrama_one("а роза упала на лапу азора", "а роза упала на лапу тризора"))


def anagrama_two(s_one: str, s_two: str)->bool:
    length_one = len(s_one)
    length_two = len(s_two)
    if length_one == length_two:
        dict_one = {}
        dict_two = {}
        pos = 0
        while length_one > pos:
            dict_one[s_one[pos]] = dict_one.get(s_one[pos], 0) + 1
            dict_two[s_two[pos]] = dict_two.get(s_two[pos], 0) + 1
            pos += 1
        if dict_one == dict_two:
            return True
    return False


t = Timer('anagrama_two("а роза упала на лапу азора", "а роза упала на лапу азора")',
          'from __main__ import anagrama_two')
print('{0:.6f}'.format(t.timeit(number=1)))

print(anagrama_two("а роза упала на лапу азора", "а роза упала на лапу азора"))
print(anagrama_two("а роза упала на лапу азора", "а роза упала на лапу тризора"))


def anagrama_three(s_one: str, s_two: str)->bool:
    if len(s_one) != len(s_two):
        return False
    list_one = [0] * 26
    list_two = [0] * 26
    pos_one = 97
    for char in s_one:
        pos_two = ord(char) - pos_one
        list_one[pos_two] += 1
    for char in s_two:
        pos_two = ord(char) - pos_one
        list_two[pos_two] += 1
    for i in list_one:
        if list_one[i] != list_two[i]:
            return False
    return True


t = Timer('anagrama_three("whatwillhappenifiwillmakeamistake", "whatwillhappenifiwillmakeamistake")',
          'from __main__ import anagrama_three')
print('{0:.6f}'.format(t.timeit(number=1)))

print(anagrama_three("whatwillhappenifiwillmakeamistake", "whatwillhappenifiwillmakeamistake"))
print(anagrama_three("whatwillhappenifiwillmakeamistake", "whatwillhappenifiwillmakeamistakeoops"))

