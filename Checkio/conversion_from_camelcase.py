#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ваша задача - написать функцию, которая преобразовывает текст (название другой функции) из формата CamelCase,
# принятого в JavaScript (MyFunctionName) в формат, принятый в Python (my_function_name), где все буквы - маленькие, а
# слова соединены знаком нижнего подчеркивания "_".
# Входные данные: Название функции как строка в CamelCase
# Output: То же самое название, но в under_score
# Как это используется: Чтобы применять названия функций в том стиле, в каком они приняты в определенном языке
# (Python, JavaScript, и т.д.).
# Предусловия :
# 0 < len(string) <= 100
# Во входящих данных не будет чисел или пустых строк
def from_camel_case(name: str) -> str:
    for i in range(1, len(name)):
        if name[i].isupper():
            name = name[:i] + '_' + name[i].lower() + name[i + 1:]
    return name.lower()


print(from_camel_case("MyFunctionName"))  # "my_function_name"
print(from_camel_case("IPhone"))          # "i_phone"

