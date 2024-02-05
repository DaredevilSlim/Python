#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Принудительное генерирование исключения
try:
    raise ValueError('Oпиcaниe исключения')
except ValueError as msg:
    print(msg)  # Выведет: Описание исключения
