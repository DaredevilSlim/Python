#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В этой миссии Ваша задача состоит в том, чтобы урезать предложение до длины, которая не превышает заданное количество
# символов.
# Если данное предложение уже достаточно короткое, Вам не нужно ничего с ним делать. В случае, если его нужно урезать,
# отсутствующая часть должна быть обозначена присоединением многоточия ("...") к концу сокращенного предложения.
# Сокращенное предложение может содержать целые слова и пробелы.
# Оно не должно содержать ни усеченных слов, ни конечных пробелов.
# Многоточие было учтено при расчете разрешенного количества символов, поэтому оно не засчитывается в счет заданной
# длины.
# Входные данные: Два аргумента:
# однострочное предложение в виде строка
# максимальная длина усеченного предложения в виду int
# Выходные данные: Урезанное предложение с многоточием (если требуется) в виде одной строки.
# Предварительное условие:
# line.startswith(' '))  # False
# 0 < len(line) ≤ 79
# 0 < length ≤ 76
# all(char in string.ascii_letters + ' ' for char in line)
def cut_sentence(line: str, length: int) -> str:
    """
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    """
    l = line[:length + 1]
    return '...' if ' ' not in l else l if len(line) <= length else l[:-1 - l[::-1].index(' ')] + '...'


print(cut_sentence("Hi my name is Alex", 8))   # "Hi my..."
print(cut_sentence("Hi my name is Alex", 4))   # "Hi..."
print(cut_sentence("Hi my name is Alex", 20))  # "Hi my name is Alex"
print(cut_sentence("Hi my name is Alex", 18))  # "Hi my name is Alex"
print(cut_sentence('Hi my name is Alex', 11))  # 'Hi my name...'
print(cut_sentence('Hi my name is Alex', 10))  # 'Hi my name...'
print(cut_sentence('Hi my name is Alex', 1))   # '...'
