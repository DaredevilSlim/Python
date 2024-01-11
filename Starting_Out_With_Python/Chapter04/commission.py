#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа вычисляет торговые комиссионные.
# Создать переменную для управления циклом.
keep_going = 'д'
# Вычислить серию комиссионных вознаграждений.
while keep_going == 'д':
    # Получить продажи продавца и его ставку комиссионных.
    sales = float(input('Введите объем продаж: '))
    comm_rate = float(input('Введите ставку комиссионных: '))
    # Рассчитать комиссионное вознаграждение.
    commission = sales * comm_rate
    # Показать комиссионное вознаграждение.
    print(f'Комиссионное вознаграждение составляет ${commission:,.2f}.')
    # Убедиться, что пользователь хочет вычислить еще одно вознаграждение.
    keep_going = input('Хотите вычислить еще одно ' +
                       '(Введите д, если да): ')