#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Листинг 2.8. Извлечение данных из отдельных групп
text_data = """101, Homework; Complete physics and math
some random nonsense
102, Laundry; Wash all the clothes today
54, random; record
103, Museum; All about Egypt
1234, random; record
Another random record"""

regex = re.compile(r'(\d{3}), (\w+); (.+)')
tasks = []
for line in text_data.split('\n'):
    match = regex.match(line)
    if match:
        task = (match.group(1), match.group(2), match.group(3))  # Создает кортеж из нескольких групп
        tasks.append(task)

print(tasks)
