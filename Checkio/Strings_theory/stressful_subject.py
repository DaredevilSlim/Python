#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# У Софии был очень напряженный месяц и она решила взять отпуск на неделю. Чтобы избежать стресса во время отпуска, она
# хочет перенаправлять Стивену электронные письма со стрессовыми темами.
# Функция должна распознавать является ли тема письма стрессовой. Стрессовая тема определяется тем, что все буквы в
# верхнем регистре, и / или заканчиваются как минимум тремя восклицательными знаками, и / или содержат по крайней мере
# одно из следующих слов-маркеров: "help", "asap", "urgent". Любое из этих слов-маркеров может быть написано по-разному:
# «HELP», «help», «HeLp», «H! E! L! P!», «H-E-L-P», и даже очень непринужденно «HHHEEEEEEEEELLP».
# Входные данные: Тема письма в виде строки.
# Выходные данные: Boolean.
# Предварительное условие:
# Тема может содержать до 100 букв.
def is_stressful(subj: str) -> bool:
    if subj and ('!!!' == subj[-3:] or subj.isupper()):
        return True
    s = 'i'
    for i in subj:
        i = i.lower()
        if i.isalpha() and i != s[-1]:
            s += i
    for i in ('help', 'asap', 'urgent'):
        if i in s:
            return True
    return False


print(is_stressful("Hi"))  # False
print(is_stressful("I neeed HELP"))  # True
print(is_stressful("I neeed HLEP"))  # False
