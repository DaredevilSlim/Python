#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа делит одно число на другое.
def main():
    # Получить два числа.
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите еще одно число: '))
    # Разделить num1 на num2 и показать результат.
    result = num1 / num2
    print(f'{num1} деленное на {num2} равно {result}')


# Вызвать главную функцию.
if __name__ == '__main__':
    main()
