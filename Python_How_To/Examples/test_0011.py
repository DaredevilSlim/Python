#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Листинг 3.2. Объект list, содержащий внутренние объекты dict
tasks = [
    {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
    {'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5},
    {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}
]

tasks.sort()
# Traceback (most recent call last):
#   File "./Examples/test_0011.py", line 11, in <module>
#     tasks.sort()
#     ~~~~~~~~~~^^
# TypeError: '<' not supported between instances of 'dict' and 'dict'
