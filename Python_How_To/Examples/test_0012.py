#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Листинг 3.3. Сортировка списков методом sort
numbers = [12, 4, 1, 3, 7, 5, 9, 8]
numbers.sort()  # Сортирует числа на месте
print(numbers)  # Вывод: [1, 3, 4, 5, 7, 8, 9, 12]

names = ['Danny', 'Aaron', 'Zack', 'Jennifer', 'Mike', 'David']
names.sort(reverse=True)  # Сортирует строки на месте, но в обратном порядке
print(names)  # Вывод: ['Zack', 'Mike', 'Jennifer', 'David', 'Danny', 'Aaron']

mixed = [3, 1, 2, 'John', ['c', 'd'], ['a', 'b']]
mixed.sort()
# Traceback (most recent call last):
#   File "./Examples/test_0012.py", line 14, in <module>
#     mixed.sort()
#     ~~~~~~~~~~^^
# TypeError: '<' not supported between instances of 'str' and 'int'
