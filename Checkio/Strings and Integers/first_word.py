#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# I might see a simplified version of this mission already First Word (simplified) . This mission is a little bit more
# complex as not only English letters can be in the given string.
# Дана строка и нужно найти ее первое слово.
# При решении задачи обратите внимание на следующие моменты:
# В строке могут встречаться точки и запятые
# Строка может начинаться с буквы или, к примеру, с пробела или точки
# В слове может быть апостроф и он является частью слова
# Весь текст может быть представлен только одним словом и все
# Входные параметры: Строка.
# Выходные параметры: Строка.
# How it is used: first word is a command in command line
# Precondition: text can contain a-z A-Z , . '

def first_word(text: str) -> str:
    return text.replace('.', ' ').replace(',', ' ').split()[0]


print(first_word("Hello world"))         # "Hello"
print(first_word(" a word "))            # "a"
print(first_word("don't touch it"))      # "don't"
print(first_word("greetings, friends"))  # "greetings"
print(first_word("... and so on ..."))   # "and"
print(first_word("hi"))                  # "hi"
print(first_word("Hello.World"))         # "Hello"
