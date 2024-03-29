#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа вычисляет заработную плату до удержаний.
def main():
    # Получить количество отработанных часов.
    hours = int(input('Сколько часов вы отработали? '))
    # Получить почасовую ставку оплаты труда.
    pay_rate = float(input('Введите свою почасовую ставку: '))
    # Вычислить заработную плату до удержаний.
    gross_pay = hours * pay_rate
    # Показать заработную плату.
    print(f'Заработная плата: ${gross_pay:,.2f}')


# Вызвать главную функцию.
if __name__ == '__main__':
    main()
