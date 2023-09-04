#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  # Подключаем модуля math


# Проверка существования атрибута
def hasattr_math(attr):
    if hasattr(math, attr):
        return "Атрибут существует"
    return "Атрибут не существует"


print(hasattr_math("pi"))  # Атрибут существует
print(hasattr_math("x"))   # Атрибут не существует
