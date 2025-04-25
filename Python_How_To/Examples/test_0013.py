#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Листинг 3.4. Сортировка задач с назначением аргумента key
def using_urgency_level(task):
    return task['urgency']


tasks = [
    {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
    {'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5},
    {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}
]
tasks.sort(key=using_urgency_level, reverse=True)
print(tasks)
# Выводимые строки (порядок изменен для удобства чтения):
# [{'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5},
# {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
# {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}]
