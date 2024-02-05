#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Применение третьего формата конструкции raise
try:
    x = 1 / 0
except Exception as err:
    raise ValueError() from err
