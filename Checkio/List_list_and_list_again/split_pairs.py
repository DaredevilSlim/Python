#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Iterable

# Разделите строку на пары из двух символов. Если строка содержит нечетное количество символов, пропущенный второй
# символ последней пары должен быть заменен подчеркиванием ('_').
# Входные данные: Строка.
# Выходные данные: Список или другой итеративный объект из строк.
# Предварительное условие: 0 <= len(str) <= 100


def split_pairs(text: str) -> Iterable[str]:
    text = text if len(text) % 2 == 0 else text + '_'
    return [] if not text else [text[i:i+2] for i in range(0, len(text), 2)]


print(list(split_pairs("abcd")))  # ["ab", "cd"]
print(list(split_pairs("abc")))  # ["ab", "c_"]
print(list(split_pairs("abcdf")))  # ["ab", "cd", "f_"]
print(list(split_pairs("a")))  # ["a_"]
print(list(split_pairs("")))  # []
