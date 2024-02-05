#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Обработчик контекста
class MyClass:
    def __enter__(self):
        print('Вызван метод __enter__()')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Вызван метод __exit__()')
        if exc_type is None:                 # Если исключение не возникло
            print('Исключение не возникло')
        else:                                # Если возникло исключение
            print('Value =', exc_val)
        return False                         # False - исключение не обработано, True - исключение обработано


print('Последовательность при отсутствии исключения:')
with MyClass():
    print('Блок внутри with')
print('\nПоследовательность при наличии исключения:')
with MyClass() as obj:
    print('Блок внутри with')
    raise TypeError('Исключение TypeError')
