#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Функция должна принимать два положительных числа (length и width) в качестве входных данных и возвращать периметр
# прямоугольника.
# Входные данные: Два целых числа (int).
# Выходные данные: Целое число (int).
# Как это может использоваться:
# в архитектурных и инженерных программах для вычисления периметров зданий или комнат;
# в компьютерной графике для вычисления периметра прямоугольника на экране;
# Предусловия:
# length, width ∈ R;
# length, width > 0.
def rectangle_perimeter(length: int, width: int) -> int:
    return int(2 * (width + length))


print(rectangle_perimeter(2, 4))  # 12
print(rectangle_perimeter(3, 5))  # 16
print(rectangle_perimeter(10, 20))  # 60
print(rectangle_perimeter(7, 2))  # 18
print(rectangle_perimeter(1, 1))  # 4
print(rectangle_perimeter(1, 5))  # 12
print(rectangle_perimeter(4, 1))  # 10
print(rectangle_perimeter(100, 100))  # 400
print(rectangle_perimeter(0.5, 2))  # 5
