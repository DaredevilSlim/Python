#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа показывает итоговый объем продаж из файла sales_data.txt.
def main():
    # Инициализировать накопитель.
    total = 0.0
    try:
        # Открыть файл sales_data.txt.
        infile = open('sales_data.txt', 'r')
        # Прочитать значения из файла
        # и накопить их в переменной.
        for line in infile:
            amount = float(line)
            total += amount
        # Закрыть файл.
        infile.close()
        # Напечатать итог.
        print(f'{total:,.2f}')
    except IOError:
        print('Произошла ошибка при попытке прочитать файл.')
    except ValueError:
        print('В файле найдены нечисловые данные.')
    except:
        print('Произошла ошибка.')


# Вызвать главную функцию.
if __name__ == '__main__':
    main()
