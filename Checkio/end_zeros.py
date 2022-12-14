#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Попробуйте выяснить какое количество нулей содержит данное число в конце.
# Входные данные: Положительное целое число (int).
# Выходные данные: Целое число (int).
def end_zeros(a: int) -> int:
    return len(str(a)) - len(str(a).rstrip('0'))


print(end_zeros(0))         # 1
print(end_zeros(1))         # 0
print(end_zeros(10))        # 1
print(end_zeros(101))       # 0
print(end_zeros(245))       # 0
print(end_zeros(100100))    # 2
