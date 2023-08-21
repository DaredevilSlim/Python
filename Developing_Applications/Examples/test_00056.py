#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использование функций globals() и locals()
def func():
    local1 = 54
    glob2 = 25
    print('Глобальные идентификаторы внутри функции')
    print(sorted(globals().keys()))
    print('Локальные идентификаторы внутри функции')
    print(sorted(locals().keys()))


glob1 = 10
glob2 = 88
func()
print('Глобальные идентификаторы вне функции')
print(sorted(globals().keys()))
