#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа демонстрирует оператор in применительно к списку.
def main():
    # Создать список номеров изделий.
    prod_nums = ['V475', 'F987', 'Q143', 'R688']
    # Получить искомый номер изделия.
    search = input('Введите номер изделия: ')
    # Определить, что номер изделия имеется в списке.
    if search in prod_nums:
        print(f'{search} найден в списке.')
    else:
        print(f'{search} не найден в списке.')


# Вызвать главную функцию.
if __name__ == '__main__':
    main()
