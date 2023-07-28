#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Требуется обратить порядок букв в каждом слове предоставленной строки, так чтобы слова остались на своих местах.
# Входные данные: строка.
# Выходные данные: строка.
# Предусловие: Строка состоит только из символов алфавита и пробелов.
def backward_string_by_word(text: str) -> str:
    return ''.join(i[::-1] for i in text.replace(' ', ', ,').split(','))


print(backward_string_by_word(""))                           # ''
print(backward_string_by_word("world"))                      # 'dlrow'
print(backward_string_by_word("hello world"))                # 'olleh dlrow'
print(backward_string_by_word("hello   world"))              # 'olleh   dlrow'
print(backward_string_by_word("welcome to a game"))          # 'emoclew ot a emag'
# print(backward_string_by_word('ha ha ha   this is cool'))  # 'ah ah ah   siht si looc'
print(backward_string_by_word('olleH Hello'))                # 'Hello olleH'
