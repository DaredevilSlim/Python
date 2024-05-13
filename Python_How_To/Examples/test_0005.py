#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Листинг 2.5. Обработка текстовых данных с разбиением строк
task_data = """1001,Homework,5
1002,Laundry,3
1003,Grocery,4"""
processed_tasks = []
for data_line in task_data.split('\n'):
    processed_task = data_line.split(',')  # Разбивает текст каждой строки
    processed_tasks.append(processed_task)

print(processed_tasks)  # [['1001', 'Homework', '5'], ['1002', 'Laundry', '3'], ['1003', 'Grocery', '4']]
