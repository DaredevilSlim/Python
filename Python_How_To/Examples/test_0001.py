#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Листинг 2.1. Создание строкового вывода с применением конкатенации строк
# Существующие переменные
name = 'Homework'
urgency = 5
# Желательный вывод: Name: Homework; Urgency Level: 5
task = 'Name: ' + name + '; Urgency Level: ' + str(urgency)
print(task)  # Вывод: Name: Homework; Urgency Level: 5
