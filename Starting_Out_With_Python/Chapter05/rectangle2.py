#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Функция area принимает ширину и длину прямоугольника в качестве аргументов и возвращает площадь прямоугольника.
def area(width, length):
    return width * length


# Функция perimeter принимает ширину и длину прямоугольника в качестве аргументов и возвращает периметр прямоугольника.
def perimeter(width, length):
    return 2 * (width + length)


# Функция main используется для тестирования другой функции.
def main():
    width = float(input("Введите ширину прямоугольника: "))
    length = float(input("Введите длину прямоугольника: "))
    print('Площадь равна ', area(width, length))
    print('Периметр равен ', perimeter(width, length))


# Вызываем функцию main, ТОЛЬКО если файл запускается как отдельная программа.
if __name__ == '__main__':
    main()
