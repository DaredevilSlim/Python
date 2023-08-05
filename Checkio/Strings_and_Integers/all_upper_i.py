#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Проверить все ли символы в строке являются заглавными. Если строка пустая или в ней нет букв - функция должна вернуть True.
# Входные данные: Строка.
# Выходные данные: Логический тип.
# Условия: a-z, A-Z, 1-9 и пробелы
def is_all_upper(text: str) -> bool:
    return text == text.upper()


print(is_all_upper("ALL UPPER"))                # True
print(is_all_upper("all lower"))                # False
print(is_all_upper("mixed UPPER and lower"))    # False
print(is_all_upper(""))                         # True
print(is_all_upper("444"))                      # True
print(is_all_upper("55 55 5 "))                 # True
