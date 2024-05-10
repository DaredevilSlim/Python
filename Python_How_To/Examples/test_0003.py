#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Листинг 2.3. Функция, получающая произвольный спецификатор формата

ids = [1, 2, 3]
names = ['Do homework', 'Laundry', 'Pay bills']
urgencies = [5, 3, 4]


def create_formatted_records(fmt):
    for i in range(3):
        id = ids[i]
        name = names[i]
        urgency = urgencies[i]
        print(f'{id:{fmt}}{name:{fmt}}{urgency:{fmt}}')


create_formatted_records('^15')
create_formatted_records('^18')
