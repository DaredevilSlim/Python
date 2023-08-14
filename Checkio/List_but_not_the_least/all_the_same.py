#p/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Any

# В этой миссии Вам надо определить, все ли элементы массива равны.
# Входные: Список.
# Выходные: Булево значение.
# Предусловия: все элементы входного списка хэшируются.


def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) == 1 if elements != [] else True


print(all_the_same([1, 1, 1]))     # True
print(all_the_same([1, 2, 1]))     # False
print(all_the_same([1, "a", 1]))   # False
print(all_the_same([1, 1, 1, 2]))  # False
print(all_the_same([]))            # True
print(all_the_same([1]))           # True
