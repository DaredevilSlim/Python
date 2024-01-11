#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа вычисляет розничные цены.
MARK_UP = 2.5  # Процент надбавки.
another = 'д'  # Переменная управления циклом.
# Обработать один или несколько товаров.
while another == 'д' or another == 'Д':
    # Получить оптовую стоимость товара.
    wholesale = float(input("Введите оптовую стоимость товара: "))
    # Вычислить розничную цену.
    retail = wholesale * MARK_UP
    # Показать розничную цену.
    print(f'Розничная цена: ${retail:,.2f}')
    # Повторить?
    another = input('Есть еще один товар? ' + '(Введите д, если да): ')