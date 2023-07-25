#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ошибочное переопределение встроенных идентификаторов
help(abs)
help = 10
print(help)
print(help(abs))
