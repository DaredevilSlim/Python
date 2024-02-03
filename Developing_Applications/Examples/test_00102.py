#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Перегрузка операторов сравнения
class MyClass:
    def __init__(self):
        self.x = 50
        self.arr = [1, 2, 3, 4, 5]
        
    def __eq__(self, y):   # Перегрузка оператора
        return self.x == y  # Перегрузка оператора in
        
    def __contains__(self, y):
        return y in self.arr


c = MyClass()
print('Равно' if c == 50 else 'Не равно')  # Выведет: Равно
print('Равно' if c == 51 else 'Не равно')  # Выведет: Не равно
print('Есть' if 5 in c else 'Нет')         # Выведет: Есть
