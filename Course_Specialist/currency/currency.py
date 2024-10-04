#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

table = re.compile(r'<table\s?[^<>]*>.+?</table>', re.DOTALL)
item = re.compile(r'''
    <td\b[^<>]*>(\d{2})\.(\d{2})\.(\d{4})</td>  # дата
    <td\b[^<>]*>(\d)</td>  # количество
    <td\b[^<>]*>(\d{1,3}\.\d{4})</td>  # курс к рублю
    ''', re.VERBOSE)

with open('history.html', 'rt', encoding='windows-1251') as src:
    data = src.read()

for m in item.finditer(data):
    day = m.group(1)
    month = m.group(2)
    year = m.group(3)
    scale = m.group(4)
    rate = m.group(5)
    print(f'{year}-{month}-{day} {scale} {rate}')
