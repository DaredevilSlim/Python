#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Листинг 2.4. Преобразование чисел в строки
def cast_number(number_str):
    try:
        casted_number = float(number_str)
    except ValueError:
        print(f"Couldn't cast {repr(number_str)} to a number")  # Функция repr создает строку в формате с кавычками
    else:
        print(f'Casting {repr(number_str)} to {casted_number}')


print(cast_number('1.5'))   # Casting '1.5' to 1.5
print(cast_number('2.3a'))  # Couldn't cast '2.3a' to a number
