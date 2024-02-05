#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Языковые конструкции else и finally
try:
    x = 10 / 2  # Нет ошибки
    # х = 10 / 0  # Ошибка деления на О
except ZeroDivisionError:
    print('Деление на О')
else:
    print('Блок else')
finally:
    print('Блок finally')
