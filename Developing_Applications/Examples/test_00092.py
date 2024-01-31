#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Изменение спЙска путей поиска модулей
sys.path.append(r'C:\folder1')
sys.path.insert(0, r'C:\folder2')
print(sys.path)
input()
