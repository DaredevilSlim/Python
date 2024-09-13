#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

#  Листинг 2.9. Использование именованных групп для извлечения данных
text_data = """101, Homework; Complete physics and math
some random nonsense
102, Laundry; Wash all the clothes today
54, random; record
103, Museum; All about Egypt
1234, random; record
Another random record"""

regex = re.compile(r'(?P<task_id>\d{3}), (?P<task_title>\w+); (?P<task_desc>.+)')
tasks = []
for line in text_data.split('\n'):
    match = regex.match(line)
    if match:
        task = (match.group('task_id'), match.group('task_title'), match.group('task_desc'))
        tasks.append(task)

print(tasks)
