#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import version_info

# Проверка установки
print(tuple(version_info))
try:
    raw_input()  # Python 2
except NameError:
    input()      # Python 3
