#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа вычисляет сумму значений из списка.
def main():
    # Создать список.
    numbers = [2, 4, 6, 8, 10]
    # Создать переменную для применения в качестве накопителя.
    total = 0
    # Вычислить сумму значений элементов списка.
    for value in numbers:
        total += value
    # Показать сумму значений элементов списка.
    print(f'Сумма элементов составляет {total}.')


# Вызвать главную функцию.
if __name__ == '__main__':
    main()