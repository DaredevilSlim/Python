#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использование функции vars()
def func():
    local1 = 54
    glob2 = 25
    print('Локальные идентификаторы внутри функции')
    print(sorted(vars().keys()))


glob = 10
glob2 = 10
func()
print('Глобальные идентификаторы вне функции')
print(sorted(vars() .keys()))
print('Указание объекта в качестве параметра')
print(sorted(vars(dict) .keys()))
print('Альтернативный вызов')
print(sorted(dict.__dict__.keys()))
