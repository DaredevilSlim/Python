#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа делит одно число на другое.
def main():
    # Получить два числа.
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите еще одно число: '))
    # Если переменная num2 не равна 0, то разделить num1 на num2 и показать результат.
    if num2 != 0:
        result = num1 / num2
        print(f'{num1} деленное на {num2} равно {result}')
    else:
        print('Деление на ноль невозможно.')


# Вызвать главную функцию.
if __name__ == '__main__':
    main()