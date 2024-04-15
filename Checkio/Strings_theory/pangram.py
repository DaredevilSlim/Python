#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Панграмма (Греческий:παν γράμμα, pan gramma, 'каждая буква') или предложение состоящее из разных букв алфавита,
# используя каждую букву по крайней мере один раз. Возможно, вы знакомы с хорошо известными панграммами
# 'Эй, жлоб! Где туз? Прячь юных съёмщиц в шкаф' или 'Любя, съешь щипцы, — вздохнёт мэр, — кайф жгуч',
# 'The quick brown fox jumps over the lazy dog'.
# Для этого задания, вы будете использовать латинский алфавит (A-Z). У вас есть текст с латинскими буквами и знаками
# препинания. Вы должны проверить является ли предложение панграммой или нет. Регистр не имеет значения.
# Входные данные: Текст как строка.
# Выходные данные: Является предложение панграммой или нет как логическое.
# Примеры:
# print(check_pangram('The quick brown fox jumps over the lazy dog.'))  # True
# print(check_pangram('ABCDEF'))  # False
# print(check_pangram('abcdefghijklmnopqrstuvwxyz'))  # True
# print(check_pangram('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))  # True
# Как это используется: Панграммы используют для отображения шрифтов, тестирования оборудования, развития почерка,
# каллиграфии и набора текста на клавиатуре.
# Предусловия:
# all(ch in (string.punctuation + string.ascii_letters + ' ') for ch in text);
# 0 < len(text).
def check_pangram(text: str) -> bool:
    text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    while i < len(alphabet) and alphabet[i] in text:
        i += 1
    return i == 26


print(check_pangram('The quick brown fox jumps over the lazy dog.'))  # True
print(check_pangram('ABCDEF'))  # False
print(check_pangram('abcdefghijklmnopqrstuvwxyz'))  # True
print(check_pangram('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))  # True
print(check_pangram('abcdefghijklmnopqrstuvwxy'))  # False
print(check_pangram('Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!'))  # True
print(check_pangram('As quirky joke, chefs won\'t pay devil magic zebra tax.'))  # True
print(check_pangram('Six big devils from Japan quickly forgot how to walt.'))  # False
