#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Листинг 3.1. Неизменяемость объектов tuple
integers_tuple = (1, 2, 3)
integers_tuple.append(4)  # Пытается использовать несуществующий метод для объекта кортежа
# Traceback (most recent call last):
#   File "./Examples/test_0010.py", line 6, in <module>
#     integers_tuple.append(4)  # Пытается использовать несуществующий метод для объекта кортежа
#     ^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'tuple' object has no attribute 'append'

integers_tuple[0] = 'zero'  # Пытается присвоить новое значение элементу кортежа
# Traceback (most recent call last):
#   File "./Examples/test_0010.py", line 13, in <module>
#     integers_tuple[0] = 'zero'  # Пытается присвоить новое значение элементу кортежа
#     ~~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
