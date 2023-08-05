#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Верните данную строку в перевернутом виде.
# Входные данные: Строка.
# Выходные данные: Строка.
def backward_string(val: str) -> str:
    return val[::-1]


print(backward_string("val"))        # "lav"
print(backward_string(""))           # ""
print(backward_string("ohho"))       # "ohho"
print(backward_string("123456789"))  # "987654321"
