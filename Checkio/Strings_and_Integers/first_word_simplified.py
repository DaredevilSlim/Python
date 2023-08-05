#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дана строка и нужно найти ее первое слово.
# Это упрощенная версия миссии First Word , которую можно решить позднее.
# Строка состоит только из английских символов и пробелов.
# В начале и в конце строки пробелов нет.
# Входные данные: строка (str).
# Выходные данные: строка (str).
# Как это используется: Первое слово — это команда в командной строке.
# Предусловия: Текст может содержать буквы a-z, A-Z и пробелы.
def first_word(text: str) -> str:
    return text.split()[0]


print(first_word("Hello world"))                   # "Hello"
print(first_word("a word"))                        # "a"
print(first_word("greeting from CheckiO Planet"))  # "greeting"
print(first_word("hi"))                            # "hi"
