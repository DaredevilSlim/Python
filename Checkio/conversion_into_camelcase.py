#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ваша задача - написать функцию, которая преобразовывает текст (название другой функции) из формата, принятого в Python
# (my_function_name) в CamelCase, принятый в JavaScript (MyFunctionName), где первая буква каждого слова -
# большая/заглавная.
# Входные данные: Название функции как строка
# Output: То же самое название, но в CamelCase
# Как это используется: Чтобы применять названия функций в том стиле, в каком они приняты в определенном языке
# (Python, JavaScript, и т.д.).
# Предусловия :
# 0 < len(string) <= 100
# Во входящих данных не будет чисел или пустых строк
def to_camel_case(name: str) -> str:
    i = 1
    name = name[0].upper() + name[1:]
    while i < len(name):
        if name[i] == '_':
            name = name[:i] + name[i + 1].upper() + name[i + 2:]
            i += 1
        i += 1
    return name


print(to_camel_case("my_function_name"))  # "MyFunctionName"
print(to_camel_case("i_phone"))           # "IPhone"
