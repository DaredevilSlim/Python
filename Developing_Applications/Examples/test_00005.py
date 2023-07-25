#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from encodings import aliases

# Вывод списка поддерживаемых кодировок
arr = aliases.aliases
keys = list(arr.keys())
keys.sort()
for key in keys:
    print('%s => %s' % (key, arr[key]))
