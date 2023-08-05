#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими
# маркерами. Но есть несколько важных условий:
# Начальный и конечный маркеры всегда разные
# Если нет начального маркера, то началом считать начало строки
# Если нет конечного маркера, то концом считать конец строки
# Если нет ни конечного, ни начального маркера, то просто вернуть всю строку
# Если конечный маркер стоит перед начальным, то вернуть пустую строку
# Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
# Output: Строка.
# Как это используется: может использоваться для парсинга небольшой верстки
# Предусловия: не может быть более одного маркера одного типа
def between_markers(text: str, begin: str, end: str) -> str:
    """
    returns substring between two given markers
    """
    b = text.find(begin)
    e = text.find(end)
    return text[b + len(begin) if b != -1 else 0:e if e != -1 else None]


print(between_markers('What is >apple<', '>', '<'))                                       # 'apple'
print(between_markers('<head><title>My new site</title></head>', '<title>', '</title>'))  # 'My new site'
print(between_markers('No[/b] hi', '[b]', '[/b]'))                                        # 'No'
print(between_markers('No [b]hi', '[b]', '[/b]'))                                         # 'hi'
print(between_markers('No hi', '[b]', '[/b]'))                                            # 'No hi'
print(between_markers('No <hi>', '>', '<'))                                               # ''
