#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа предлагает пользователю ввести суммы продаж и записывает эти суммы в файл sales.txt.
def main():
    # Получить количество дней.
    num_days = int(input('За какое количество дней Вы располагаете продажами? '))
    # Открыть новый файл с именем sales.txt.
    sales_file = open('sales.txt', 'w')
    # Получить суммы продаж за каждый день и записать их в файл.
    for count in range(1, num_days + 1):
        # Получить продажи за день.
        sales = float(input(f'Введите продажи за день No {count}: '))
        # Записать сумму продаж в файл.
        sales_file.write(f'{sales}\n')
    # Закрыть файл.
    sales_file.close()
    print('Данные записаны в sales.txt.')


# Вызвать главную функцию.
if __name__ == '__main__':
    main()
