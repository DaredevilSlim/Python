#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дана последовательность строк. Вам нужно определить наиболее часто встречаемую строку в последовательности.
# Входные данные: список строк.
# Выходные данные: строка.
def most_frequent(data: list[str]) -> str:
    d = dict((data.count(i), i) for i in set(data))
    return d[max(d)]


print(most_frequent(["a", "b", "c", "a", "b", "a"]))  # 'a'
print(most_frequent(["a", "a", "bi", "bi", "bi"]))    # 'bi'
print(most_frequent(['a']))                           # 'a'
print(most_frequent(['a', 'a']))                      # 'a'
print(most_frequent(['a', 'a', 'z']))                 # 'a'
