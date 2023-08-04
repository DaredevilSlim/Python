#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable

# Не все элементы важны. Вам нужно удалить из список все элементы до указаного.
# На примере мы имеем список [1, 2, 3, 4, 5] где нужно было удалить все элементы до 3 - 1 и 2 соответственно.
# Есть два ньюанса: (1) если в списке нет элемента до которого нужно удалить остальные элементы, то список не должен
# измениться. (2) если list пустой, то он должен остаться пустым.
# Входные данные: Список и элемент до которого нужно удалить другие элементы.
# Выходные данные: Набор значений (кортеж, список, итератор ...).


def remove_all_before(items: list, border: int) -> Iterable:
    return items[items.index(border):] if border in items else items


print(list(remove_all_before([1, 2, 3, 4, 5], 3)))              # [3, 4, 5]
print(list(remove_all_before([1, 1, 2, 2, 3, 3], 2)))           # [2, 2, 3, 3]
print(list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)))        # [2, 4, 2, 3, 4]
print(list(remove_all_before([1, 1, 5, 6, 7], 2)))              # [1, 1, 5, 6, 7]
print(list(remove_all_before([], 0)))                           # []
print(list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)))  # [7, 7, 7, 7, 7, 7, 7, 7, 7,]
