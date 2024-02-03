#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создание свойства вызовом функции property()
class MyClass:
    def get_var(self):  # Геттер
        return self.var

    def set_var(self, value):  # Сеттер
        self.var = value

    def del_var(self):  # Делетер
        del self.var

    v = property(fget=get_var, fset=set_var, fdel=del_var, doc='Свойство')


c = MyClass()
c.v = 35    # Вызывается сеттер
print(c.v)  # Вызывается геттер
del c.v     # Вызывается делетер
