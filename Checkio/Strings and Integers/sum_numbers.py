#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом. Если число является частью слова,
# то его суммировать не нужно.
# Текст состоит из чисел, пробелов и букв английского алфавита.
# Входные данные: Строка.
# Выходные данные: Целое число.
def sum_numbers(text: str) -> int:
    return sum(int(i) for i in text.split() if i.isdigit())


print(sum_numbers("hi"))  # 0
print(sum_numbers("who is 1st here"))  # 0
print(sum_numbers("my numbers is 2"))  # 2
print(sum_numbers
    ("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"))  # 3755
print(sum_numbers("5 plus 6 is"))  # 11
print(sum_numbers(""))  # 0
