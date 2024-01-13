#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа демонстрирует именованные аргументы.
def main():
    # Показать сумму простого процентного дохода, используя 0.01 как процентной ставки за период, 10 как количество
    # периодов и $10 000 как основную сумму на счете.
    show_interest(rate=0.01, periods=10, principal=10000.0)


# Функция show_interest показывает сумму простого процентного дохода для заданной основной суммы, процентной ставки
# за период и количество периодов.
def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print(f'Простой процентный доход составит ${interest:,.2f}')


# Вызвать главную функцию.
main()