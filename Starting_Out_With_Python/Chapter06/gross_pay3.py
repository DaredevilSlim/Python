#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа вычисляет заработную плату до удержаний.
def main():
    try:
        # Получить количество отработанных часов.
        hours = int(input('Сколько часов вы отработали? '))
        # Получить почасовую ставку оплаты труда.
        pay_rate = float(input('Введите почасовую ставку: '))
        # Вычислить заработную плату.
        gross_pay = hours * pay_rate
        # Показать заработную плату.
        print(f'Зарплата: ${gross_pay:,.2f}')
    except ValueError as err:
        print(err)


# Вызвать главную функцию.
if __name__ == '__main__':
    main()
