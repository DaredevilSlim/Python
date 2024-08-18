#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Листинг 2.7. Текстовые данные для обработки
text_data = """101, Homework; Complete physics and math
some random nonsense
102, Laundry; Wash all the clothes today
54, random; record
103, Museum; All about Egypt
1234, random; record
Another random record"""

regex = re.compile(r'(\d{3}), (\w+); (.+)')  # Разбивает текст по строкам данных
for line in text_data.split("\n"):
    match = regex.match(line)  # Использует метод match для поиска совпадения в начале строки
    if match:
        print(f"{'Matched:':<12}{match.group()}")  # Использует метод group для вывода текста совпадения
    else:
        print(f"{'No Match:':<12}{line}")

