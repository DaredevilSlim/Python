#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Код главной программы
from test_00085 import *
from test_00086 import *
import test_00085, test_00086
print(s)             # Выведет: "Значение из модуля test_0086"
print(test_00085.s)  # Выведет: "Значение из модуля test_0085"
print(test_00086.s)  # Выведет: "Значение из модуля test_0086"
input()
