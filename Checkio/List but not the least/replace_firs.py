#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable

# В данном списке первый элемент должен стать последним. Пустой список или список из одного элемента не должен
# измениться.
# Входные данные: Список.
# Выходные данные: Набор элементов.


def replace_first(items: list) -> Iterable:
    return items[1:] + items[:1] if len(items) > 1 else items


print(replace_first([1, 2, 3, 4]))  # [2, 3, 4, 1]
print(replace_first([1]))           # [1]
print(replace_first([]))            # []
